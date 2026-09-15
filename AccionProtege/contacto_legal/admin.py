from django.contrib import admin
from .models import SolicitudContacto


@admin.register(SolicitudContacto)
class SolicitudContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'creado', 'acepta_privacidad')
    readonly_fields = ('ip', 'creado')
