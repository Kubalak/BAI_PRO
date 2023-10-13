from django.urls import path

from .views import register_view, login_view

urlpatterns = [
    path("mainApp/register/", register_view, name="register"),
    path("mainApp/login/", login_view, name="login"),
]