from django.db import models
from .validators import validar_camposvacios, validar_logitud
from django.core.validators import EmailValidator

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.nombre
    
class Residencia(models.TextChoices):
    LOCAL = "dpto", 'LOCAL'
    NACIONAL= 'naci', 'NACIONAL'
    EXTRAJERO= 'exte', 'EXTRAJERO'

class Ganado(models.Model):
    nombre= models.CharField(max_length=30, unique=True)
    tipo =models.ForeignKey(Tipo, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255, blank=True, validators=[validar_logitud])
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    disponible = models.BooleanField(blank=True, default=True)
    Residencia = models.CharField(
        max_length=4,
        choices=Residencia.choices,
        default=Residencia.LOCAL
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Ganadero(models.Model):
    nombre= models.CharField(max_length=60)
    apellido= models.CharField(max_length=100)
    ci= models.CharField(max_length=20)
    telefono= models.CharField(max_length=20)
    celular= models.CharField(max_length=12)
    email= models.CharField(max_length=30, validators=[EmailValidator('No es un email valido')])
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    

class Zona(models.Model):
    nombre= models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Estancia(models.Model):
    nombre= models.CharField(max_length=60)
    zona= models.ForeignKey(Zona, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, blank=True )
    coordenadax= models.CharField(max_length=30)
    coordenaday= models.CharField(max_length=30)
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
     
