from django.db import models

class Mensaje(models.Model):
    contenido = models.TextField()
    usuario = models.CharField(max_length=50, default='Anonimo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    direccion_ip = models.GenericIPAddressField(null=True, blank=True)