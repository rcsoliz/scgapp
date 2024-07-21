from django.contrib import admin
from .models import Tipo, Ganado, Ganadero, Zona, Estancia
# Register your models here.
class TipoAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

class GanadoAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo', 'descripcion', 'disponible',)
    list_filter = ('disponible', 'tipo',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

class Ganaderodmin(admin.ModelAdmin):
    list_display = ('nombre','apellido', 'ci', 'telefono','celular','email', 'disponible')
    list_filter = ('disponible', 'nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

class ZonaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

class Estanciadmin(admin.ModelAdmin):
    list_display = ('nombre','zona', 'descripcion', 'coordenadax','coordenaday', 'disponible')
    list_filter = ('disponible', 'zona',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

admin.site.register(Tipo, TipoAdmin)
admin.site.register(Ganado, GanadoAdmin)
admin.site.register(Ganadero, Ganaderodmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(Estancia,Estanciadmin)
