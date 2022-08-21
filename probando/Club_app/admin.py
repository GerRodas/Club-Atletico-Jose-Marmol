from django.contrib import admin

############IMPORTO LOS MODELOS  ####

from Club_app.models import Avatar, Profesores, Alumnos, Actividades
#LIST DISPLAY PARA MOSTRAR EN COLUMNAS
#search para buscar en todas las columnas
class Alumnosadmin(admin.ModelAdmin):
    list_display = ["nombre","edad","actividad","turno"]
    search_fields = ["nombre","edad","actividad","turno"]

class Profesoresadmin(admin.ModelAdmin):
    list_display = ["nombre","actividad","turno"]
    search_fields = ["nombre","actividad","turno"]
class Actividadesadmin(admin.ModelAdmin):
    list_display = ["actividad","turno"]
    search_fields = ["actividad","turno"]

# Register your models here.
admin.site.register(Profesores, Profesoresadmin)
admin.site.register(Alumnos, Alumnosadmin)
admin.site.register(Actividades, Actividadesadmin)
admin.site.register(Avatar)

#USUARIO pisto
#clave 123456

#Usuario creado desde el front 
#Zaira
#clave: holamundo

admin.site.site_header = 'Club Atlético José Mármol'
admin.site.index_title = 'Panel de administración'
admin.site.site_title = 'Club Atlético José Mármol'