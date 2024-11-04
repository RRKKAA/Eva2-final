from django.shortcuts import render
from EvaApp.forms import (formVideojuego, formUsuario, formComputadora)
from EvaApp.models import (videojuego, usuario, computadora)

# Create your views here.

def index(request):
    return render(request,"index.html")

def listadoUsuarios(request):
    usuarios = usuario.objects.all()
    data = {'usuarios':usuarios}
    return render(request,"listadoUsuarios.html",data)

def agregarUsuario(request):
    form = formUsuario()
    if request.method == 'POST':
        form = formUsuario(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,"agregarUsuario.html",data)

def actualizarUsuario(request, id):
    usuario = usuario.objects.get(id = id)
    form = formUsuario(instance=usuario)
    if request.method == 'POST':
        form = formUsuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,"agregarUsuario.html",data)

def eliminarUsuario(request, id):
    usuario = usuario.objects.get(id = id)
    usuario.delete()
    return redirect("/usuarios")





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
    return render(request,"agregarVideojuego.html",data)

def eliminarJuego(request, id):
    videojuego = videojuego.objects.get(id = id)
    videojuego.delete()
    return redirect("/videojuegos")



def listadoComputadoras(request):
  computadoras = computadora.objects.all()
  data = {'computadoras': computadoras}
  return render(request, "listadoComputadoras.html", data)

def agregarComputadora(request):
  form = formComputadora()
  if request.method == 'POST':
    form = formComputadora(request.POST)
    if form.is_valid():
      form.save()
      return listadoComputadoras(request)
  data = {'form': form}
  return render(request, "agregarComputadora.html", data)

def actualizarComputadora(request, id):
  computadora = computadora.objects.get(pk=id)
  form = formComputadora(instance=computadora)
  if request.method == 'POST':
    form = formComputadora(request.POST, instance=computadora)
    if form.is_valid():
      form.save()
      return listadoComputadoras(request)
  data = {'form': form}
  return render(request, "agregarComputadora.html", data)

def eliminarComputadora(request, id):
  computadora = computadora.objects.get(pk=id)
  computadora.delete()
  return redirect("/computadoras")

def detalleUsuario():