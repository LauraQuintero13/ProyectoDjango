from django.shortcuts import render,redirect
from appTienda.models import Categoria,Producto
from django.db import Error

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def vistaCategoria(request):
    return render(request, "frmCategoria.html")

def agregarCategoria(request):
    nombre = request.POST["txtNombre"]
    try:
        categoria = Categoria(catNombre = nombre)
        categoria.save()
        mensaje="Categoria Agregada Correctamente"
    except Error as error:
        mensaje=f"Problemas al Agregar {error}"
    retorno = {"mensaje":mensaje}
    return render(request, "frmCategoria.html",retorno)

def listarProductos(request):
    try:
        productos = Producto.objects.all()
        mensaje=""
    except Error as error:
        mensaje=f"Problemas al Listar los Productos {error}"
    retorno = {"mensaje":mensaje, "listaProductos":productos}
    return render(request,"listarProductos.html",retorno)

def vistaProducto(request):
    try:
        categorias = Categoria.objects.all()
        mensaje=""
    except Error as error:
        mensaje=f"Problemas {error}"
    retorno = {"mensaje":mensaje, "listaCategorias":categorias, "producto":None}
    return render(request, "frmProducto.html",retorno)

def agregarProducto(request):
    nombre = request.POST["txtNombre"]
    codigo = int(request.POST["txtCodigo"])
    precio = int(request.POST["txtPrecio"])
    idCategoria = int(request.POST["cbCategoria"])
    archivo = request.FILES["fileFoto"]
    try:
        #obtener la categoria de acuerdo a su id
        categoria = Categoria.objects.get(id=idCategoria)
        #crear el producto
        producto = Producto(proNombre = nombre,proCodigo=codigo,
                            proPrecio=precio, proCategoria=categoria,
                            proFoto = archivo)
        
        producto.save()
        mensaje="Producto Agregado Correctamente"
        return redirect("/listarProductos/")
    except Error as error:
        mensaje=f"Problemas al Registrar el Producto {error}"
        
    categorias = Categoria.objects.all()
    retorno = {"mensaje":mensaje, "listaCategorias":categorias, "producto":producto}
    return render(request,"frmProducto.html",retorno)

def consultarProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        categorias = Categoria.objects.all()
        mensaje=""
    except Error as error:
        mensaje=f"Problemas {error}"
    retorno = {"mensaje":mensaje,"producto":producto,
               "listaCategorias":categorias}
    return render(request,"frmEditarProducto.html",retorno)

def actualizarProducto(request):
    idProducto = int(request.POST["idProducto"])
    nombre = request.POST["txtNombre"]
    codigo = int(request.POST["txtCodigo"])
    precio = int(request.POST["txtPrecio"])
    idCategoria = int(request.POST["cbCategoria"])
    archivo = request.FILES.get("fileFoto",False)
    try:
        #obtener la categoria de acuerdo a su id
        categoria = Categoria.objects.get(id=idCategoria)
        #actualizar el producto. PRIMERO SE CONSULTA
        producto = Producto.objects.get(id=idProducto)
        producto.proNombre=nombre
        producto.proPrecio=precio
        producto.proCategoria=categoria
        producto.proCodigo=codigo
        #si el campo de foto tiene datos actualiza foto
        if(archivo!=''):
            producto.proFoto=archivo
        producto.save()
        mensaje="Producto Actualizado Correctamente"
        return redirect("/listarProductos/")                
    except Error as error:
        mensaje =f"Problemas al realizar el proceso de actualizar el producto {error}"
    categorias = Categoria.objects.all()
    retorno = {"mensaje":mensaje,"listaCategorias":categorias,"producto":producto}
    return render(request,"frmEditarProducto.html",retorno)

def eliminarProducto(id):
    try:
        producto = Producto.objects.get(id=id)
        producto.proFoto.storage.delete(producto.proFoto.name)
        producto.delete()
        mensaje="Producto Eliminado Correctamente"
    except Error as error:
        mensaje=f"Problemas al eliminar el producto {error}"
    retorno = {"mensaje":mensaje}
    return redirect("/listarProductos/",retorno)