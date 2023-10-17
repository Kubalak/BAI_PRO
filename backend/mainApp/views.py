from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods
from django.utils.dateparse import parse_datetime
from django.shortcuts import redirect
from .forms import UserForm
from .serializers import CommentSerializer
from .models import Comment

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
        date_time = parse_datetime('2023-06-12T18:22:00Z+02:00')
    ).save()
    Comment(
        title = 'Unharmful comment',
        comment = 'This is a great example of unharmful <strong>comment</strong> with injected HTML &lt;strong&gt; tag.',
        date_time = parse_datetime('2023-08-15T15:32:10Z+02:00')
    ).save()
    Comment(
        title = 'Somewhat dangerous comment',
        comment = 'This is a great example of dangerous comment <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ?si=O7ynaNQw9GcNtXud" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> with injected HTML &lt;iframe&gt; tag.',
        date_time = parse_datetime('2023-09-08T22:40:31Z+02:00')
    ).save()
    Comment(
        title = 'Pretty dangerous comment',
        comment = 'This is a great example of dangerous comment with <img src onerror="alert(\'injected <script> tag\')"/>',
        date_time = parse_datetime('2023-10-09T00:20:15Z+02:00')
    ).save()
    Comment(
        title = 'Extremly dangerous comment',
        comment = '<img src onerror="fetch(\'http://localhost:8000/main/js/\').then(response => response.text()).then( text => document.write(text)).catch(error => { })">',
        date_time = parse_datetime('2023-10-12T21:37:00Z+02:00')
    ).save()
    return JsonResponse({"message": "Comments generated successfully"})


@require_http_methods(["GET"])
def domcompromise(request):
    return HttpResponse('<html><body>You see compromised DOM <a href="/">Go home</a></body></html>')