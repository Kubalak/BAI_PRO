from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.views.decorators.http import require_http_methods

def index(request):
    return HttpResponse("Hello there from index!")

# @csrf_exempt
def register_view(request):
    if request.method == 'POST':
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
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
# @csrf_exempt
def login_view(request):
    if request.method == 'POST':
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
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@require_http_methods(["GET"])
def test(request:HttpRequest):
    return JsonResponse({"data": [i for i in range(1,20)], "authenticated": request.user.is_authenticated})

@require_http_methods(['GET'])
def islogin(request):
    return JsonResponse({"authenticated": request.user.is_authenticated})