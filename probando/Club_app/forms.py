from dataclasses import field, fields
from django import forms

from .models import Profesores, Avatar

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class ProfesorFormulario(forms.ModelForm):
    nombre=forms.CharField(max_length=40)
    actividad=forms.CharField(max_length=40)
    turno=forms.CharField(max_length=40)
    imagen=forms.ImageField()

    class Meta:
        model= Profesores
        fields=("imagen",)

class AlumnoFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    edad=forms.CharField(max_length=40)
    actividad=forms.CharField(max_length=40)
    turno=forms.CharField(max_length=40)


class ActividadesFormulario(forms.Form):
    actividad=forms.CharField(max_length=40)
    turno=forms.CharField(max_length=40)


class UserEditForm(UserCreationForm):

    #password = forms.CharField(
        #help_text="",
        #widget=forms.HiddenInput(), required=False
    #)
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    last_name = forms.CharField(label="Nombre")
    first_name = forms.CharField(label="Apellido")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reingrese contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2","username"]

        help_texts = {k:"" for k in fields}

    #def clean_password2(self):

        #password2 = self.cleaned_data["password2"]
        #if password2 != self.cleaned_data["password1"]:
            #raise forms.ValidationError("Contraseñas diferentes")
        #return password2



class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)