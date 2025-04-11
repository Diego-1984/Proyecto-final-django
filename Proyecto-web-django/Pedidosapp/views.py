from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, LineaPedidos
from Carroapp.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url="/autenticacion/logearse")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items:
        lineas_pedido.append(LineaPedidos(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))
    enviar_mail(
        pedido= pedido,
        lineas_pedido = lineas_pedido,
        nombre_usuario = request.user.username,
        email_usuario = request.user.email
    )
    messages.success(request, "El pedido se ha realizado correctamente")
    return redirect("../tienda")

# No está configurado para enviar email. Solo implementada lógica
def enviar_mail(**kwargs):
    asunto = "Gracias por su pedido"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usuario": kwargs.get("nombre_usuario")
    })
    mensaje_de_texto = strip_tags(mensaje)
    from_email = "diegomenoruceta@gmail.com"
    to = kwargs.get("email_usuario")

    send_mail(asunto, mensaje_de_texto, from_email, [to], html_message=mensaje)
