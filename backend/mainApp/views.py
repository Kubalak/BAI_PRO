from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods

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

@require_http_methods(["GET"])
def test(request:HttpRequest):
    return JsonResponse({"data": [i + 1 for i in range(20)], "authenticated": request.user.is_authenticated})

@require_http_methods(['GET'])
@ensure_csrf_cookie  # Zapewnia że ciastko zostanie wysłane podczas sprawdzania stanu użytkownika.
def islogin(request):
    return JsonResponse({"authenticated": request.user.is_authenticated})