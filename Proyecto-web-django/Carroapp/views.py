from django.shortcuts import render, redirect
from .carro import Carro
from Tiendapp.models import Producto
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Agregar producto al carrito
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    
    messages.success(request, f'🛒 {producto.nombre} agregado al carrito')
    return redirect(request.META.get('HTTP_REFERER', 'Tienda'))

# Eliminar producto del carrito
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("carro:Carro")

# Restar cantidad de producto
def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("carro:Carro")

# Limpiar el carrito completo
def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    messages.success(request, "¡Pedido realizado correctamente!")
    return redirect("carro:Carro")

# Vista protegida del carrito
@login_required(login_url='logearse')
def carro(request):
    return render(request, "carro/carro.html")
