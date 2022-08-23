from email.mime import image
from enum import auto
import django
from django.template import loader
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from Club_app.models import Actividades, Alumnos, Profesores
from Club_app.forms import ProfesorFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def inicio(self):
    return render(self, "inicio.html")


def profesores(request):

    if request.method == "POST":

        profesores = Profesores(nombre=request.POST["nombre"], actividad=request.POST["actividad"], turno=request.POST["turno"], imagen=request.POST["imagen"])
        
        profesores.save()

        return render(request,"cargaexitosa.html")

    return render(request,"profesores.html")



def actividades(request):
    
    if request.method == "POST":

        actividades = Actividades(actividad=request.POST["actividad"], turno=request.POST["turno"])
        
        actividades.save()

        return render(request,"cargaexitosa.html")

    return render(request,"actividades.html")


def alumnos(request):
    
    if request.method == "POST":

        alumnos = Alumnos(nombre=request.POST["nombre"], edad=request.POST["edad"],actividad=request.POST["actividad"], turno=request.POST["turno"])
        
        alumnos.save()

        return render(request,"cargaexitosa.html")

    return render(request,"alumnos.html")



def listado_actividades(request):

    lista = Actividades.objects.all()

    dic = {"activ":lista} 

    plantilla = loader.get_template("listadoactividades.html")
    
    documento = plantilla.render(dic)

    return HttpResponse(documento)

#otra forma hubiese sido, dejo lista y sigue con:
#contexto =  {"activ":lista}
# return render(request,"listadoactividades.html", contexto)


### BUSQUEDA de profesores que dictan clases de: / LA BUSQUEDA EN LA COLUMANA ACTIVIDAD

def busqueda_profesor(request):

    return render(request,"busquedaprofesor.html")

# BUSCANDOPROFE SE RENDERIZA EN RBUSQUEDAPROFESOR  / ESTA DEF LA MODIQUE EL 17/08 A LO QUE VIMOS EN CLASE PORQUE QUERIA RECUPERAR LA IMAGEN
def buscando_profe(request):

    if request.GET["actividad"]:

        actividad = request.GET["actividad"]

        otroscampos = Profesores.objects.all()

        profesores = Profesores.objects.filter(actividad__icontains=actividad)

        return render(request, "rbusquedaprofesor.html",  {"profesores": profesores, "actividad": actividad})

    else:
        mensaje = "No se ingreso parametros de busqueda"
        return HttpResponse(mensaje)



#PRACTICANDO CLASE 22

@staff_member_required(login_url="/Club_app/solostaff/")
def listaprofesores(request):

    profesores = Profesores.objects.all()
    contexto = {"profesores": profesores}

    return render(request, "leerProfesores.html", contexto)


@login_required
def crea_profesor(request):


    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST,request.FILES)

        if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data

            profesor = Profesores(nombre=data["nombre"], actividad=data["actividad"], turno=data["turno"], imagen=data["imagen"])
       

        profesor.save()

        return render(request, "cargaexitosa.html")

    else:
        miFormulario = ProfesorFormulario()

        
    return render(request, "profesorFormulario.html", {"miFormulario": miFormulario})





def eliminarprofesor(request, id):

    if request.method == "POST":

        profesor = Profesores.objects.get(id=id)
        profesor.delete()
        profesores = Profesores.objects.all()
        contexto = {"profesores": profesores}

        return render(request, "leerProfesores.html", contexto)


def editar_profesor(request,id):

    print("method:", request.method)
    print("post:", request.POST)

    profesor = Profesores.objects.get(id=id)

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            profesor.nombre = data["nombre"]
            profesor.actividad = data["actividad"]
            profesor.turno = data["turno"]
            profesor.imagen =data["imagen"]

            profesor.save()

            return render(request, "cargaexitosa.html")

    else:
        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "actividad": profesor.actividad,
            "turno": profesor.turno,
            "imagen": profesor.imagen})

        
    return render(request, "editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})


    #CLASE 23  LOGIN LOGOUT Y REGISTRARARSE

def loginView(request):

    if request.method == "POST":

        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return render(request, "inicio.html", {"mensaje": f"Bienvendido {usuario}"})

            else:

                return render (request, "inicio.html", {"mensaje": "Error, datos incorrectos"})
        
        return render (request, "inicio.html", {"mensaje": "Error, datos incorrectos"})
        
    else:

        miFormulario = AuthenticationForm()

    return render(request, "login.html", {"miFormulario": miFormulario})



def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "inicio.html", {"mensaje": f"Usuario {username} creado"})
    
    else:

        form = UserCreationForm()

    return render(request, "registro.html", {"miFormulario": form})



def loginrequerido(request):
    
    return render(request, "loginrequerido.html")


def solo_staff(request):
    
    return render(request, "solostaff.html")




def contacto(request):

    if request.method == "POST":

        subject=request.POST["asunto"]

        message=request.POST["mensaje"] + " " + request.POST["email"]

        email_from=settings.EMAIL_HOST_USER

        recipient_list=["josemarmol262@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "emailenviado.html")

    return render(request, "contacto.html")






       

           


