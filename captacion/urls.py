from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tipos', views.TipoViewSet)
router.register(r'ganados', views.GanadoViewSet)
router.register(r'estancias', views.EstanciaViewSet)

urlpatterns = [
  #  path("", views.index, name="index"),
  #path('contact/<str:name>/', views.contact, name='contact'),
  #path('tipos/', views.tipos, name='tipos'),
  #path('tipos/', views.tipos, name='tipos'),
  #path('ganados/', views.ganadoFormView, name='ganados'),
  #path('index/', views.index),

  #path('', include(router.urls),)
  path('tipos/', views.TipoCreateView.as_view()),
  path('estancias/cantidad/', views.estancia_count),
  path('ganados/filtrar/procedencia', views.ganado_procedencia),
  path("ganados/reporte/", views.reporte_ganados),
]
