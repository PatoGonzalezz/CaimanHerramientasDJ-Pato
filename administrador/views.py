from django.shortcuts import render
from .models import Tipo, Producto
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q
from .forms import TipoForm
# Create your views here.


def register(request):
    return render(request,"registration/register.html")

@login_required
def menu (request):
    request.session["usuario"]="pato"
    usuario = request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, "inicioadmin.html",context)

@login_required
def inicio (request):
    lista_productos = Producto.objects.all()
    context={"productos":lista_productos}
    return  render(request,'inicioadmin.html', context)


def lista_productos(request):
    busqueda = request.GET.get("buscar")
    lista_productos = Producto.objects.raw("SELECT * FROM administrador_Producto")

    if busqueda:
        lista_productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) | 
            Q(id_producto__icontains = busqueda)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator (lista_productos, 5)
        lista_productos = paginator.page(page)
    except:
        raise Http404
    context = {"productos":lista_productos}
    return render(request,'inicioadmin.html',context)


def agregar_productos(request):
    if request.method != "POST":
        lista_tipo =  Tipo.objects.all()
        context =  {"tipos":lista_tipo}
        return render(request, 'productos_add.html', context)
    else:
        id_prod         = request.POST["id"]
        nombre_prod     = request.POST["nombre"]
        marca_prod      = request.POST["marca"]
        tipo            = request.POST["tipo"]
        imagen          = request.FILES["imagen"]
        precio_prod     = request.POST["precio"]
        stock_prod      = request.POST["stock"]

        objTipoProducto =  Tipo.objects.get(id_tipo = tipo)
        objProducto     = Producto.objects.create(
            id_producto     = id_prod,
            nombre          = nombre_prod,
            marca           = marca_prod,
            id_tipo         = objTipoProducto,
            foto_producto   = imagen,
            precio          = precio_prod,
            stock           = stock_prod)

        objProducto.save()
        messages.success(request, "Producto Agregado")
        lista_tipo = Tipo.objects.all()
        context = {"tipos":lista_tipo}
        return render(request, 'productos_add.html',context)

def eliminar_productos(request,pk):
    
    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete() #delete en la BD
        messages.success(request,"Producto Eliminado")
        lista_producto = Producto.objects.all()
        context={"productos":lista_producto}
        return render(request,'inicioadmin.html',context)
    except:
        lista_producto = Producto.objects.all()
        context={"productos":lista_producto}
        return render(request,'inicioadmin.html',context)

def buscar_productos(request,pk):
    if pk != "":
        producto = Producto.objects.get(id_producto=pk)
        tipos = Tipo.objects.all()
        context={"producto":producto, "tipos":tipos}
        if producto:
            return render(request,'productos_edit.html', context)
        else:
            context = {"mensaje":"El producto no existe"}
            return render(request,'inicioadmin.html',context)    

def actualizar_productos(request):
    
    if request.method == "POST":
        #rescatamos en variables los valores del formulario (name)
        id_prod         = request.POST["id"]
        nombre_prod     = request.POST["nombre"]
        marca_prod      = request.POST["marca"]
        tipo            = request.POST["tipo"]
        imagen          = request.FILES["imagen"]
        precio_prod     = request.POST["precio"]
        stock_prod      = request.POST["stock"]

        objTipo = Tipo.objects.get(id_tipo = tipo)
        #crea Producto (izd: nombre del campo de la BD, derecho: variable local)
        objProducto = Producto()
        objProducto.id_producto   = id_prod
        objProducto.nombre        = nombre_prod
        objProducto.marca         = marca_prod
        objProducto.id_tipo       = objTipo
        objProducto.foto_producto = imagen
        objProducto.precio        = precio_prod
        objProducto.stock         = stock_prod
        
        objProducto.save() #update en la base de datos
        messages.success(request, "Producto Actualizado")
        lista_Producto = Producto.objects.all()
        lista_tipo = Tipo.objects.all()
        context = {"tipos":lista_tipo,"productos":lista_Producto}
        return render(request,'inicioadmin.html',context)
    else:
        lista_Producto = Producto.objects.all()
        context = {"productos":lista_Producto}
        return render(request,'productos_edit.html',context)
    
def lista_tipos(request):
    busqueda = request.GET.get("buscar")
    lista_tipos = Tipo.objects.all()
    
    if busqueda:
        lista_tipos = Tipo.objects.filter(
            Q(tipo__icontains = busqueda) |
            Q(id_tipo__icontains = busqueda)
        ).distinct()
    context={"tipos":lista_tipos}
    return render(request,'listaTipos.html',context)    

def agregar_tipo(request):
    if request.method == "POST":
        form = TipoForm(request.POST)
        if form.is_valid:
            form.save() #insert
            messages.success(request, "Tipo Agregado")
            form = TipoForm()
            context = {"mensaje": "Se agrego el tipo", "form":form}
            return render(request,'tipos_add.html',context)
    else:
        form = TipoForm()
        context = {"form":form}
        return render(request,'tipos_add.html',context)
    
def borrar_tipo(request,pk):
    errores = []
    try:
        tipo = Tipo.objects.get(id_tipo=pk)
        if tipo:
            tipo.delete()
            messages.success(request,"Tipo Eliminado")
            lista_tipos = Tipo.objects.all() 
            context = {"mensaje": "Tipo eliminado", "tipos":lista_tipos, "errores": errores}
            return render(request,'listaTipos.html',context)
    except:
        lista_tipos = Tipo.objects.all() 
        context = {"mensaje": "No existe el tipo", "tipos":lista_tipos, "errores": errores}
        return render(request,'listaTipos.html',context)

def buscar_tipo(request,pk):
    if pk != 0:
        tipo = Tipo.objects.get(id_tipo=pk)
        context={"tipo":tipo}
        if tipo:
            return render(request,'tipos_edit.html',context)
        else:
            context = {"mensaje":"El tipo no existe"}
            return render(request,'listaTipos.html',context)

def actualizar_tipo(request):
        if request.method == "POST":
            id_tipo         = request.POST["id"]
            nombre_tipo     = request.POST["nombre"]
            
            #crea Producto (izd: nombre del campo de la BD, derecho: variable local)
            objTipo = Tipo()
            objTipo.id_tipo = id_tipo
            objTipo.tipo    = nombre_tipo
            
            objTipo.save() #update en la base de datos
            messages.success(request, "Tipo Actualizado")
            lista_tipo = Tipo.objects.all()
            context = {"tipos":lista_tipo}
            return render(request,'listaTipos.html',context)
        else:
            lista_tipo = Tipo.objects.all()
            context = {"tipos":lista_tipo}
            return render(request,'tipos_edit.html',context)  