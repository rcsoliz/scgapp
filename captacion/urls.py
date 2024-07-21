from django.urls import path, include
from .import views

urlpatterns = [
  #  path("", views.index, name="index"),
  path('contact/<str:name>/', views.contact, name='contact'),
  #path('tipos/', views.tipos, name='tipos'),
  path('tipos/', views.tipos, name='tipos'),
  path('ganados/', views.ganadoFormView, name='ganados'),
  path('index/', views.index),
]
