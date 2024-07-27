from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tipo,Ganado,Zona, Ganadero, Estancia
from .form import GanadoForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import TipoSerializer, GanadoSerializer,EstanciaSerializer,ReporteGanadoSerializer
from rest_framework import generics
from rest_framework.decorators import api_view

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

    return render(request, "form_ganados.html", {"form": 
    form})

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class GanadoViewSet(viewsets.ModelViewSet):
    queryset= Ganado.objects.all()
    serializer_class = GanadoSerializer

class EstanciaViewSet(viewsets.ModelViewSet):
    queryset= Estancia.objects.all()
    serializer_class = EstanciaSerializer

class TipoCreateView(generics.DestroyAPIView, generics.ListAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

@api_view(['GET'])
def estancia_count(request):
    """
    Cuenta la cantidad de __estancias__
    """
    try:
        cantidad = Estancia.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad,
            },
            safe = False,
            status = 200,
        )

    except Exception as e:
        return JsonResponse(
            {
                "error": str(e),
            },
            safe=False,
            status=400
        )
    
@api_view(['GET'])
def ganado_procedencia(request):
    """
    Lista el ganado en procedencia __ganado__
    """
    try:
        ganados = Ganado.objects.filter(Residencia = "naci")
        return JsonResponse(
            GanadoSerializer(ganados, many=True).data,
            safe = False,
            status = 200,
        )

    except Exception as e:
        return JsonResponse(
            {
                "message": str(e),
            },
            safe=False,
            status=400
        )
    
@api_view(['GET'])
def reporte_ganados(request):
    """
    Lista de ganado filtrados en mercado departamental
    """

    try:
        ganados = Ganado.objects.filter(Residencia = "dpto")
        cantidad = ganados.count()
        return JsonResponse(
            ReporteGanadoSerializer({
                "cantidad": cantidad,
                'clases': ganados,
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )