from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nueva():
    return 0

def index(request):
    #return HttpResponse("Bienvenido")
    return render(request, 'index.html')

def procesamiento(request):
    nombre = request.POST['nombre']
    nombre = nombre.title()
    return render(request,'proceso.html', {'name':nombre})
    #vas a invocar una página html que se llama "proceso"
    #le vas a pasar una variable que se llama "name" cuyo contenido es un nombre
    #desde el punto de vista de Python es un diccionario


