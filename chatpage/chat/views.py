from django.shortcuts import render, redirect
from .models import Mensaje

def home(request):
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    print("Client IP:", client_ip)
    if request.method == 'POST':
        contenido = request.POST.get('message-input')
        usuario = request.POST.get('username-input')

        if usuario == '':
            usuario = "Anónimo"

        if contenido:
            mensaje = Mensaje(contenido=contenido, usuario=usuario)
            mensaje.save()

        return redirect('home')

    mensajes = Mensaje.objects.all().order_by('-fecha_creacion')

    if mensajes.count() > 10:
        mensaje_ultimo = mensajes.first()
        mensajes.exclude(pk=mensaje_ultimo.pk).delete()

    mensajes = Mensaje.objects.all().order_by('-fecha_creacion')
    return render(request, 'index.html', {'mensajes': mensajes})


