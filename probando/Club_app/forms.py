from dataclasses import field
from django import forms

from .models import Profesores


class ProfesorFormulario(forms.ModelForm):
    nombre=forms.CharField(max_length=40)
    actividad=forms.CharField(max_length=40)
    turno=forms.CharField(max_length=40)
    imagen=forms.ImageField()

    class Meta:
        model= Profesores
        fields=("imagen",)