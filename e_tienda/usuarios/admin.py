from django.contrib import admin
from .models import Cliente, Administrador
from usuarios.models import Estado, Municipio


admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Estado)
admin.site.register(Municipio)
