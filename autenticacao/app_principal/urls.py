from django.urls import path, include
from app_principal import views

app_name = "app_principal"

urlpatterns = [
    path('', views.PrincipalView.as_view(), name="principal"),
    path('pagina/um/', views.PaginaUm.as_view(), name="pagina_um"),
    path('pagina/dois/', views.PaginaDois.as_view(), name="pagina_dois"),
    path('usuarios/', include('app_usuarios.urls')),
]
