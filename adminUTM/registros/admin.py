from django.contrib import admin
from .models import AdministrarEmpleados 
from .models import ComentarioContacto
from .models import RegistroSolicitudes

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'nombre', 'apellidoPa', 'apellidoMa', 'area')

admin.site.register(AdministrarEmpleados, AdministrarModelo)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

class AdministrarRegistroSolicitudes(admin.ModelAdmin):
    list_display = ('id', 'matricula')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated')

admin.site.register(RegistroSolicitudes, AdministrarRegistroSolicitudes)