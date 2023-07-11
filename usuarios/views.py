from django.shortcuts import render, redirect

from administrador.models import Producto, Tipo
from usuarios.carrito import Carrito

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    return render(request, "index.html", {'productos':productos})

def agregar_producto(request, pk):
    
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=pk)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=pk)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=pk)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def quienSomos(request):
    return render(request, "about.html")

def registro(request):
    return render(request, "register.html")

def prods(request):
    productos = Producto.objects.all()
    return render(request, "productos.html",{'productos':productos})

def carrito(request):
    return render(request, "shop.html")

def marcas(request):
    return render(request,"marcas.html")

