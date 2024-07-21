from django.urls import path
from .import views

urlpatterns = [
  #  path("", views.index, name="index"),
  path('contact/<str:name>/', views.contact, name='contact'),
  path('tipos/', views.tipos, name='tipos'),
  path('index/', views.index),
]
