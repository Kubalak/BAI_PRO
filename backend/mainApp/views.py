from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods
from django.utils.dateparse import parse_datetime
from .forms import UserForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from backend import settings
from .serializers import CommentSerializer
from .models import Comment
import sqlite3
from traceback import format_exc

def index(request):
    return HttpResponse("Hello there from index!")

@require_http_methods(['POST'])
def register_view(request):
    
    try:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        form = UserForm({
                'username': username,
                'email': email,
                'password1': password1,
                'password2': password2
        })
        
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User registered successfully.'})
        else:
            return JsonResponse({'error': form.errors}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    
@require_http_methods(["POST"])
def login_view(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return JsonResponse({'message':'User logged in sucessfully'})
        else:
            return JsonResponse({'error':'Invalid username or password'}, status=400)
    except Exception as e:
        return JsonResponse({'error':str(e)}, status=500)
    

def logout_view(request):
    logout(request)
    return JsonResponse({'message':'User logged out'})


@require_http_methods(['GET'])
@ensure_csrf_cookie  # Zapewnia że ciastko zostanie wysłane podczas sprawdzania stanu użytkownika.
def islogin(request):
    return JsonResponse({"authenticated": request.user.is_authenticated})


@require_http_methods(['GET'])
def comments(request:HttpRequest):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Please log in first!"}, status=401)
    return JsonResponse({"comments": CommentSerializer(Comment.objects.all(), many=True).data})


@require_http_methods(['POST'])
@csrf_exempt
def gen_comments(request):
    if Comment.objects.count() >= 5:
        return JsonResponse({"message": "Already created"})
    Comment(
        title = 'Simple comment',
        comment = 'This is a great example of normal comment',
        date_time = parse_datetime('2023-06-12T18:22:00+02:00')
    ).save()
    Comment(
        title = 'Unharmful comment',
        comment = 'This is a great example of unharmful <strong>comment</strong> with injected HTML &lt;strong&gt; tag.',
        date_time = parse_datetime('2023-08-15T15:32:10+02:00')
    ).save()
    Comment(
        title = 'Somewhat dangerous comment',
        comment = 'This is a great example of dangerous comment <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ?si=O7ynaNQw9GcNtXud" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> with injected HTML &lt;iframe&gt; tag.',
        date_time = parse_datetime('2023-09-08T22:40:31+02:00')
    ).save()
    Comment(
        title = 'Pretty dangerous comment',
        comment = 'This is a great example of dangerous comment with <img src onerror="alert(\'injected <script> tag\')"/>',
        date_time = parse_datetime('2023-10-09T00:20:15+02:00')
    ).save()
    Comment(
        title = 'Extremly dangerous comment',
        comment = '<img src onerror="fetch(\'http://localhost:8000/main/js/\').then(response => response.text()).then( text => document.write(text)).catch(error => { })">',
        date_time = parse_datetime('2023-10-12T21:37:00+02:00')
    ).save()
    return JsonResponse({"message": "Comments generated successfully"})


@require_http_methods(["GET"])
def domcompromise(request):
    return HttpResponse('<html><body>You see compromised DOM <a href="javascript:window.location.reload(true)">Go home</a></body></html>')

@require_http_methods(["POST"])
def create_sample(request):
    try:
        file = open("start.sql", "r")
        conn = sqlite3.connect('sample.sqlite3')
        cursor = conn.cursor()
        cursor.executescript(file.read())
        cursor.close()
        conn.close()
        file.close()
        return JsonResponse({"message": "Sample database created successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@require_http_methods(["GET"])
def getsql(request:HttpRequest):
    try:
        conn = sqlite3.connect('sample.sqlite3')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        result = None
        name = request.GET['name'] if 'name' in request.GET else ''
        if 'safe' in request.GET and request.GET['safe'] == 'true':
            result = cursor.execute("""
            SELECT 
                name, 
                price, 
                thumbnail 
            FROM 
                products 
            WHERE 
                name LIKE ?
            """,
                (f'%{name}%',)
            )
        else:
            result = cursor.execute(f"SELECT name, price, thumbnail FROM products WHERE name LIKE '%{name}%'")
        # IMPORTANT #
        # WE ASSUME DEV IS LAZY AND WANTED TO GET EVERY COLUMN FROM QUERY AND RETURN IT TO USER #
        products = [{item: row[item] for item in row.keys()} for row in result]
        cursor.close()
        conn.close()
        return JsonResponse({"products": products, "query": f"SELECT name, price, thumbnail FROM products WHERE name LIKE '%{name}%'"})
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e), "stack": format_exc()}, status=500)

# @require_http_methods(['POST']) # LAZY DEV DIDN'T SELECT REQUIRED METHOD
def render_mail(request:HttpRequest):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized. Please log in first!"}, status=401)
    try:
        html = get_template('email.html')
        txt = get_template('email.txt')
        subject, _from, to = 'Important information', settings.EMAIL_HOST_USER, request.user.email
        html_content = html.render({'username': request.user.username})
        text_content = txt.render({'username': request.user.username})
        msg = EmailMultiAlternatives(subject, text_content, _from, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except Exception as e:
        print(e)
        return JsonResponse({"error": "Unable to send email!"}, status=500)
 
    return JsonResponse({"message": "Email sent successfully!"})