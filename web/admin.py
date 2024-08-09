from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import SolicitudVecino, Vecino, Distrito, ZonaUrb, CalleAv, FichaOperativa, Solicitudes, generate_random_code
from django.utils.html import format_html


@admin.register(SolicitudVecino)
class SolicitudVecinoAdmin(admin.ModelAdmin):
    list_display = ('vecino', 'distrito', 'zona_urbanizacion', 'ubicacion_direccion', 'latitud', 'longitud', 'celular', 'google_maps_link')
    search_fields = ('vecino__codigo_usuario', 'ubicacion_direccion', 'distrito__nombre', 'zona_urbanizacion__nombre')  # Ajusta según tus campos
    list_filter = ('distrito', 'zona_urbanizacion')
    ordering = ('fecha',)  # Cambiado de 'codigo' a 'fecha'
    
    fieldsets = (
        (None, {
            'fields': ('vecino', 'distrito', 'zona_urbanizacion', 'ubicacion_direccion', 'celular')
        }),
        ('Ubicación Geográfica', {
            'fields': ('latitud', 'longitud')
        }),
    )

    def google_maps_link(self, obj):
        if obj.latitud and obj.longitud:
            url = obj.get_google_maps_url()
            return format_html(f'<a href="{url}" target="_blank">Ver en Google Maps</a>')
        return '-'
    google_maps_link.short_description = 'Ubicación en el mapa'

class VecinoAdmin(admin.ModelAdmin):
    readonly_fields = ('codigo_usuario',)

    def save_model(self, request, obj, form, change):
        if not obj.codigo_usuario:
            obj.codigo_usuario = generate_random_code()
        super().save_model(request, obj, form, change)

admin.site.register(Vecino, VecinoAdmin)
# Registrar los otros modelos

admin.site.register(ZonaUrb)
admin.site.register(Distrito)
admin.site.register(CalleAv) 
admin.site.register(FichaOperativa)
admin.site.register(Solicitudes)



