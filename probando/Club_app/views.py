from email.mime import image
from enum import auto
import django
from django.template import loader
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from Club_app.models import Actividades, Alumnos, Profesores, Avatar
from Club_app.forms import ActividadesFormulario, AlumnoFormulario, ProfesorFormulario, UserEditForm, AvatarFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.



def inicio(request):

    try:
       avatar = Avatar.objects.get(user=request.user.id)
       return render(request, "inicio.html", {"url": avatar.imagen.url})

    except:
        return render(request, "inicio.html")


def alumnos(request):


    if request.method == "POST":

        miFormulario = AlumnoFormulario(request.POST)

        if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data

            Alumno = Alumnos(nombre=data["nombre"], edad=data["edad"], actividad=data["actividad"], turno=data["turno"])
       
            Alumno.save()

            return render(request, "cargaexitosa.html")

    else:
        miFormulario = AlumnoFormulario()

        
    return render(request, "alumnoFormulario.html", {"miFormulario": miFormulario})



def lista_alumnos(request):

    alumnos = Alumnos.objects.all()
    contexto = {"alumnos": alumnos}

    return render(request, "listaalumnos.html", contexto)


@staff_member_required(login_url="/Club_app/solostaff/")
def eliminar_alumnos(request, id):

    if request.method == "POST":

        alumno = Alumnos.objects.get(id=id)
        alumno.delete()
        alumnos = Alumnos.objects.all()
        contexto = {"alumnos": alumnos}

        return render(request, "listaalumnos.html", contexto)


@login_required
def editar_alumno(request,id):

    alumno = Alumnos.objects.get(id=id)

    if request.method == "POST":

        miFormulario = AlumnoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            alumno.nombre = data["nombre"]
            alumno.edad = data["edad"]
            alumno.actividad = data["actividad"]
            alumno.turno =data["turno"]

            alumno.save()

            return render(request, "cargaexitosa.html")

    else:
        miFormulario = AlumnoFormulario(initial={
            "nombre": alumno.nombre,
            "edad": alumno.edad,
            "actividad": alumno.actividad,
            "turno": alumno.turno})

        
    return render(request, "editarAlumno.html", {"miFormulario": miFormulario, "id": alumno.id})



@login_required
def crear_actividad(request):


    if request.method == "POST":

        miFormulario = ActividadesFormulario(request.POST)

        if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data

            Activ = Actividades(actividad=data["actividad"], turno=data["turno"])
       
            Activ.save()

            return render(request, "cargaexitosa.html")

    else:
        miFormulario = ActividadesFormulario()

        
    return render(request, "actividadFormulario.html", {"miFormulario": miFormulario})


def listado_actividades(request):

    actividades = Actividades.objects.all()
    contexto = {"actividades": actividades}

    return render(request, "listaactividades.html", contexto)

@staff_member_required(login_url="/Club_app/solostaff/")
def eliminar_actividad(request, id):

    if request.method == "POST":

        actividad = Actividades.objects.get(id=id)
        actividad.delete()
        actividades = Actividades.objects.all()
        contexto = {"actividades": actividades}

        return render(request, "listaactividades.html", contexto)


#@staff_member_required(login_url="/Club_app/solostaff/")
def editar_actividad(request,id):

    actividad = Actividades.objects.get(id=id)

    if request.method == "POST":

        miFormulario = ActividadesFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            actividad.actividad = data["actividad"]
            actividad.turno = data["turno"]

            actividad.save()

            return render(request, "cargaexitosa.html")

    else:
        miFormulario = ActividadesFormulario(initial={
            "actividad": actividad.actividad,
            "turno": actividad.turno})


        
    return render(request, "editarActividad.html", {"miFormulario": miFormulario, "id": actividad.id})







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





@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data


            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.username = data["username"]

            usuario.save()

            return render(request, "perfilactualizado.html")

    else:

        miFormulario = UserEditForm(initial={"email":usuario.email, "first_name": usuario.first_name,"last_name": usuario.last_name,"username": usuario.username})

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario":usuario})



@login_required
def agregar_avatar(request):

    if request.method == "POST":
        
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            #esta parte la arme como la filminas
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data["imagen"])

            #avatar = Avatar(user=request.user, imagen=data['imagen'])

            avatar.save()

        return render(request, "inicio.html")

    else:

        miFormulario = AvatarFormulario()

    return render(request, "agregarAvatar.html", {"miFormulario": miFormulario})



#def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]

            usuario.save()

            return render(request, "perfilactualizado.html")

    else:

        miFormulario = UserEditForm(instance=request.user)

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario})

def contacto(request):

    if request.method == "POST":

        subject=request.POST["asunto"]

        message=request.POST["mensaje"] + " " + request.POST["email"]

        email_from=settings.EMAIL_HOST_USER

        recipient_list=["josemarmol262@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "emailenviado.html")

    return render(request, "contacto.html")


def nosotros(request):
    
    return render(request, "nosotros.html")


def PrevioAlumnos(request):
    
    return render(request, "previoAlumnos.html")



       

           


