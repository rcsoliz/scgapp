from django.http import HttpResponse
from django.shortcuts import render
from .models import Tipo

def index(request):
    return HttpResponse("Hola Roberto")

def contact(request, name):
    return HttpResponse(f"Bienvendo {name} a la clase de Django")

def tipos(request):
    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
       items = Tipo.objects.filter(nombre__contains=filtro_nombre)
    else:
        items = Tipo.objects.all()
    
    return render(request, "tipos.html", {"tipos": items})
