from django.urls import path
from django.contrib.auth import views as auth_view

app_name = "app_usuarios"

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name="login_usuario"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),
]
