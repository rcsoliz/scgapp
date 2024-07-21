from django.http import HttpResponse
from django.shortcuts import render
from .models import Tipo,Ganado,Zona, Ganadero, Estancia
from .form import GanadoForm
from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse("Hola Roberto")

def contact(request, name):
    return HttpResponse(f"Bienvendo {name} a la clase de Django")

def tipos(request):
    post_nombre = request.POST.get("nombre")
    if post_nombre:
        q = Tipo(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
       items = Tipo.objects.filter(nombre__contains=filtro_nombre)
    else:
        items = Tipo.objects.all()
    
    return render(request, "form_tipos.html", {"tipos": items})

def ganadoFormView(request):
    form = GanadoForm()
    ganado = None
    id_ganado = request.GET.get("id")
    if id_ganado:
        ganado = get_object_or_404(Ganado,id=id_ganado)
        form = GanadoForm(instance=ganado)

    if request.method == "POST":
        if ganado:
            form = GanadoForm(request.POST, instance=ganado)
        else:
            form = GanadoForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_ganados.html", {"form": form})

