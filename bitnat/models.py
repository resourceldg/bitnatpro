from __future__ import unicode_literals

from django.db import models


class Contacto(models.Model):
        nombre = models.CharField(max_length=50)
        email = models.EmailField(max_length=150)
        telefono = models.CharField(max_length=30)
        empresa = models.CharField(max_length=70)
        mensaje = models.CharField(max_length=500)
        fecha = models.DateTimeField(auto_now_add=True, blank=True)
