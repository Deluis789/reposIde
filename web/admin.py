from django.contrib import admin
from .models import ZonaUrb, Distrito, CalleAv, SolicitudVecino, SolicitudTecnica, Solicitudes
# Register your models here.

admin.site.register(ZonaUrb)
admin.site.register(Distrito)
admin.site.register(CalleAv)
admin.site.register(SolicitudVecino)
admin.site.register(SolicitudTecnica)
admin.site.register(Solicitudes)