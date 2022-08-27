from distutils.command.upload import upload
from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Alumnos(models.Model):

    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    actividad=models.CharField(max_length=40)
    turno=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} - {self.edad} - {self.actividad} - {self.turno}"
    class Meta():
        ordering = ("nombre", "edad", "actividad", "turno")

        
class Profesores(models.Model):

    nombre=models.CharField(max_length=40)
    actividad=models.CharField(max_length=40)
    turno=models.CharField(max_length=40)
    imagen= models.ImageField(upload_to="profesores", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.actividad} - {self.turno}"

    class Meta():
        ordering = ("nombre", "actividad", "turno")

class Actividades(models.Model):

    actividad=models.CharField(max_length=40)
    turno=models.CharField(max_length=40)
    

    def __str__(self):
        return f"{self.actividad} - {self.turno}"

    class Meta():
        ordering = ("actividad", "turno")
#unique evita que se repitan registros
        unique_together = ("actividad", "turno")



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", blank=True, null=True)

class Noticias(models.Model):
    titulo = models.CharField(max_length=60)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fechaPublicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    def get_absolute_url(self):
        return reverse('noticias')