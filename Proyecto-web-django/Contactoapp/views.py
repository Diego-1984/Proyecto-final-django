from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")

            email = EmailMessage("Mensaje desde App de Django", "El usuario con nombre {} "
            "con la dirección {} escribe lo siguiente:\n\n{}".format(nombre,email,mensaje), "", 
            ["dimenoruceta@hotmail.com"], reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")

            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                return redirect("/contacto/?novalido")
                    
    
    return render(request, "contacto/contacto.html",{"miFormulario":formulario_contacto})