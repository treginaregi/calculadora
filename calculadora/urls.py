from django.urls import path
from . import views
#Sirve para importar la clase views que está en el directorio actual

urlpatterns = [
    path('', views.index, name = 'index'),
    path('procesamiento', views.procesamiento, name = 'procesamiento'),
    path('suma', views.suma, name = 'suma'),
    path('resta', views.resta, name = 'resta'),
    path('multiplicacion', views.multiplicacion, name = 'multiplicacion'),
    path('division', views.division, name = 'division'),
    path('usuarios', views.usuarios, name = 'usuarios'),
    path('usuarios_p', views.usuarios_p, name = 'usuarios_p'),
    path('usuarios_d', views.usuarios_d, name = 'usuarios_d'),
    path('usuarios_u', views.usuarios_u, name = 'usuarios_u'),
]