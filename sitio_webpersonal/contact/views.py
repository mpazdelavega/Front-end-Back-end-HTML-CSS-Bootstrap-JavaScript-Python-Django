from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage 
from .models import Registrado
# Create your views here.

def contacto(request):
    #print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Crear el correo que se enviara 
            email = EmailMessage(
                "Future Tourism : nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["ch.lin@alumnos.duoc.cl"],
                reply_to = [email]
            )
            registrado = Registrado(name=contact_form.cleaned_data['name'],
                                    email=contact_form.cleaned_data['email'],
                                    content=contact_form.cleaned_data['content'])
            registrado.save()

            try:
                email.send()
                return redirect(reverse('contacto') + "?OK")
            except:
                return redirect(reverse('contacto') + "?FAIL")
    return render(request, "contact/contacto.html", {'form':contact_form})


