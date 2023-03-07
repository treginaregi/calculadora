from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3

class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)

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
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
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
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
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
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num_resultado = num1 * num2
    den_resultado = den1 * den2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num_resultado = num1 * den2
    den_resultado = den1 * num2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def usuarios(request):
    if request.method == 'GET':
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM usuarios")
        resultado = res.fetchall()
        return render(request, 'datos.html',{'lista_usuarios':resultado})
        #Ver otra opción en repositorio del profe
    elif request.method == 'POST':
        body = request.body.decode('utf-8')
        eljson = loads(body)
        grado = eljson['grado']
        grupo = eljson['grupo']
        num_lista = eljson['num_lista']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES (?,?,?)", (grupo, grado, num_lista))
        con.commit()
        return HttpResponse("Usuario agregado")
    elif request.method == 'DELETE':
        return(usuarios_d(request))

@csrf_exempt
def usuarios_p(request):
    body = request.body.decode('utf-8')
    eljson = loads(body)
    grado = eljson['grado']
    grupo = eljson['grupo']
    num_lista = eljson['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES (?,?,?)", (grupo, grado, num_lista))
    con.commit()
    return HttpResponse("Usuario agregado")

@csrf_exempt
def usuarios_d(request):
    body = request.body.decode('utf-8')
    eljson = loads(body)
    grado = eljson['grado']
    grupo = eljson['grupo']
    num_lista = eljson['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("DELETE FROM usuarios WHERE grupo = ? AND grado = ? AND num_lista = ?", (grupo, grado, num_lista))
    con.commit()
    return HttpResponse("Usuario borrado")

@csrf_exempt
def usuarios_u(request):
    body = request.body.decode('utf-8')
    eljson = loads(body)
    grado = eljson['grado']
    grupo = eljson['grupo']
    num_lista = eljson['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("DELETE FROM usuarios WHERE grupo = ? AND grado = ? AND num_lista = ?", (grupo, grado, num_lista))
    con.commit()
    return HttpResponse("Usuario borrado")