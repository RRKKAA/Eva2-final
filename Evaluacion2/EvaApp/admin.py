from django.contrib import admin
from EvaApp.models import videojuego

class videojuegoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'publicador', 'genero', 'tamanio', 'costo']

# Register your models here.
admin.site.register(videojuego, videojuegoAdmin)