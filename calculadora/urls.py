from django.urls import path
from . import views
#Sirve para importar la clase views que está en el directorio actual

urlpatterns = [
    path('', views.index, name = 'index'),
    path('procesamiento', views.procesamiento, name = 'procesamiento'),
]