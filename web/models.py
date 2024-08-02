from django.db import models

# # Create your models here.
# class User(models.Model):
#     codigo_usuario = models.CharField(max_length=8, null=False, blank=False)
#     nombre = models.CharField(max_length=50, null=False, blank=False)
#     apellido_paterno = models.CharField(max_length=50, null=False, blank=False)
#     apellido_materno = models.CharField(max_length=50, null=False, blank=False)
#     ci = models.CharField(max_length= 10, null=False, blank=False)
#     rol = models.CharField(max_length= 50, null=False, blank=False)

#     def __str__(self):
#         return self.nombre

# class Roles(models.Model):
#     usuario = models.ForeignKey(User, on_delete=models.RESTRICT)
#     nombre = models.CharField(max_length=50, null=False, blank=False)
#     fecha = models.DateTimeField(auto_now_add=True) 

class ZonaUrb(models.Model):
    nombre = models.CharField(max_length=80, null=False, blank=False)
    descripcion = models.TextField()
    ciudad = models.CharField(max_length=50, default='El alto')
    cordenadas = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre
    
class Distrito(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.nombre

class CalleAv(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=True)
    numero_vivienda = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.nombre


class SolicitudVecino(models.Model):
    codigo = models.CharField(max_length=10, blank=False, null=False, default='AAA')
    distrito = models.ForeignKey(Distrito, on_delete=models.RESTRICT)
    zona_urbanizacion = models.ForeignKey(ZonaUrb, on_delete=models.RESTRICT)
    ubicacion_direccion = models.CharField(max_length=100, null=False, blank=False)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    celular = models.IntegerField()

    def __str__(self):
        return self.codigo

class SolicitudTecnica(models.Model):

    ESTADO_OPCIONES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
        
    distrito = models.ForeignKey(Distrito, on_delete=models.RESTRICT)
    zonaurb = models.ForeignKey(ZonaUrb, on_delete=models.RESTRICT)
    codigo = models.CharField(default='AAA', null=False, blank=False)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    maquinaria = models.CharField(max_length=50, null=True, blank=True)
    operador = models.CharField(max_length=100, null=True, blank=True)
    volumen = models.CharField(max_length=100, null=True, blank=True)
    descripcion_trabajo = models.TextField(default='Descripcion...')
    foto_inicio = models.ImageField(upload_to='trabajo', blank=True)
    foto_desarollo = models.ImageField(upload_to='trabajo', blank=True)
    foto_culminado = models.ImageField(upload_to='trabajo', blank=True)
    estado = models.CharField(max_length=30, choices=ESTADO_OPCIONES, default='pendiente')

    def __Str__(self):
        return f'{self.codigo} - {self.get_estado_display()}'
    
class Solicitudes(models.Model):

    ESTADO_OPCIONES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    solicitud_vecino = models.ForeignKey(SolicitudVecino, on_delete=models.RESTRICT)
    solicitud_tecnica = models.ForeignKey(SolicitudTecnica, on_delete=models.RESTRICT)
    descripcion = models.TextField(null=True)
    estado = models.CharField(max_length=30, choices=ESTADO_OPCIONES, default='pendiente')
    def __Str__(self):
        return f'{self.get_estado_display()}'