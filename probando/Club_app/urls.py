from django.urls import path

from Club_app.views import actividades, alumnos, buscando_profe, contacto, crea_profesor, editar_profesor, eliminarprofesor, inicio, listaprofesores, profesores, busqueda_profesor, listado_actividades, loginView, register, loginrequerido, solo_staff

from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("", inicio),
    path("Club_app/profesores/", profesores, name="profesores"),
    path("Club_app/busquedaprofesor/", busqueda_profesor, name="busquedaprofesor"),
    path("Club_app/buscandoprofe/", buscando_profe, name="buscandoprofe"),
    path("Club_app/actividades/", actividades, name="actividades"),
    path("Club_app/alumnos/", alumnos, name="alumnos"),
    path("Club_app/listaactividades/", listado_actividades, name="listaactividades"),
    path("Club_app/leerprofesores/",listaprofesores, name="listaprofesores"),
    path("Club_app/eliminarprofesor/<int:id>", eliminarprofesor, name="eliminarprofesor"),
    path("edita-profesor/<int:id>", editar_profesor, name="editarProfesor"),
    path("crea-profesor/", crea_profesor, name="CreaProfesor"),
    path("Club_app/login/", loginView, name="Login"),
    path("Club_app/registrar/", register, name="Registrar"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("Club_app/loginrequerido/", loginrequerido, name="loginrequerido"),
    path("Club_app/solostaff/", solo_staff, name="solostaff"),
    path("Club_app/contacto/", contacto, name="contacto"),

]
