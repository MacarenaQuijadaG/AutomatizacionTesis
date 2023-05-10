from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here

admin.site.register(Campus)
admin.site.register(Documento)
admin.site.register(DetalleAsignacion)
admin.site.register(Capitulo)
admin.site.register(Item)
admin.site.register(Imagen)
admin.site.register(Observacion)
admin.site.register(Anexo)
@admin.register(Bibliografia)
class BibliografiaAdmin(admin.ModelAdmin):
    pass
