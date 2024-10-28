from django.shortcuts import render
from EvaApp.forms import formVideojuego
from EvaApp.models import videojuego

# Create your views here.

def index(request):
    return render(request,"index.html")

def listadoVideojuegos(request):
    videojuegos = videojuego.objects.all()
    data = {'videojuegos':videojuegos}
    return render(request,"listadoVideojuegos.html",data)

def agregarJuego(request):
    form = formVideojuego()
    if request.method == 'POST':
        form = formVideojuego(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,"agregarVideojuego.html",data)

def actualizarJuego(request, id):
    videojuego = videojuego.objects.get(id = id)
    form = formVideojuego(instance=videojuego)
    if request.method == 'POST':
        form = formVideojuego(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,"actualizarJuego.html",data)

def eliminarJuego(request, id):
    videojuego = videojuego.obects.get(id = id)
    videojuego.delete()
    return redirect("/videojuegos")