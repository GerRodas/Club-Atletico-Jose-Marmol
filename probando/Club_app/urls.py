from django.urls import path


from Club_app.views import AgregarNoticia, AgregarNoticia, EditarNoticia, EliminarNoticia, NoticiasDetalle, agregar_avatar, alumnos, buscando_profe, crea_profesor, crear_actividad, editar_actividad, editar_alumno, editar_perfil, editar_profesor, eliminar_actividad, eliminar_alumnos, eliminarprofesor, inicio, lista_alumnos, listaprofesores, busqueda_profesor, listado_actividades, loginView, register, loginrequerido, solo_staff




from django.contrib.auth.views import LogoutView

from Club_app.views import contacto, nosotros, PrevioAlumnos, NoticiasView



urlpatterns = [
    path("", inicio, name= "inicio"),
    #no lo utilizamos path("Club_app/profesores/", profesores, name="profesores"),
    path("Club_app/busquedaprofesor/", busqueda_profesor, name="busquedaprofesor"),
    path("Club_app/buscandoprofe/", buscando_profe, name="buscandoprofe"),
    path("Club_app/actividades/", crear_actividad, name="actividades"),
    path("Club_app/alumnos/", alumnos, name="creaalumnos"),
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
    path("Club_app/editarperfil/", editar_perfil, name="editarperfil"),
    path("Club_app/agregaravatar/", agregar_avatar, name="agregaravatar"),
    path("Club_app/listaalumnos/", lista_alumnos, name="listaalumnos"),
    path("Club_app/eliminaralumnos/<int:id>", eliminar_alumnos, name="eliminaralumnos"),
    path("Club_app/editaralumnos/<int:id>", editar_alumno, name="editarAlumnos"),
    path("Club_app/eliminaractividad/<int:id>", eliminar_actividad, name="eliminaractividad"),
    path("Club_app/editaractividad/<int:id>", editar_actividad, name="editarActividad"),
    path("Club_app/contacto/", contacto, name="contacto"),
    path("Club_app/nosotros/", nosotros, name="nosotros"),
    path("Club_app/previoAlumnos/", PrevioAlumnos, name="previoAlumnos"),
    path("Club_app/noticias/", NoticiasView.as_view(), name="noticias"),
    path("Club_app/detallenoticia/<int:pk>/", NoticiasDetalle.as_view(), name="detallenoticia"),
    path("Club_app/agregarnoticia/", AgregarNoticia.as_view(), name="agregarnoticia"),
    path("Club_app/editarnoticia/<int:pk>/", EditarNoticia.as_view(), name="editarnoticia"),
    path("Club_app/eliminarnoticia/<int:pk>/", EliminarNoticia.as_view(), name="eliminarnoticia"),

]

