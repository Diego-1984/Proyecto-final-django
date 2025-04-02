from django.shortcuts import render, redirect
from .carro import Carro
from Tiendapp.models import Producto
from django.contrib import messages

# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    
    messages.success(request, f'🛒 {producto.nombre} agregado al carrito')

    return redirect(request.META.get('HTTP_REFERER', 'Tienda'))

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto=producto)
    return redirect("carro:Carro")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.restar_producto(producto=producto)
    return redirect("carro:Carro")

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("carro:Carro")

def carro(request):
    return render(request, "carro\carro.html")