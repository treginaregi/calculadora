from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps

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

@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['num1']
    den1 = body['den1']
    num2 = body['num2']
    den2 = body['den2']
    if den1 == den2:
        num_resultado = num1 + num2
        den_resultado = den1
    else:
        den_resultado = den1 * den2
        num_resultado = int(((den_resultado/den1)*num1) - ((den_resultado/den2)*num2))
    resultado = Fraccion(num_resultado,den_resultado)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, content_type = "text/json-comment-filtered")

@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['num1']
    den1 = body['den1']
    num2 = body['num2']
    den2 = body['den2']
    if den1 == den2:
        num_resultado = num1 - num2
        den_resultado = den1
    else:
        den_resultado = den1 * den2
        num_resultado = int(((den_resultado/den1)*num1) - ((den_resultado/den2)*num2))
    resultado = Fraccion(num_resultado,den_resultado)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, content_type = "text/json-comment-filtered")

@csrf_exempt
def multiplicacion(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['num1']
    den1 = body['den1']
    num2 = body['num2']
    den2 = body['den2']
    num_resultado = num1 * num2
    den_resultado = den1 * den2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['num1']
    den1 = body['den1']
    num2 = body['num2']
    den2 = body['den2']
    num_resultado = num1 * den2
    den_resultado = den1 * num2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")


