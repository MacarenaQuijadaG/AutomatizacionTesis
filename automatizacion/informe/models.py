from django.db import models
from usuario.models import Usuario

# Create your models here.

class Campus(models.Model):
    sede = models.CharField(max_length=10)
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.sede

class Documento(models.Model):
    portada = models.CharField(max_length=1000)
    sumario = models.CharField(max_length=10000)
    introduccion = models.CharField(max_length=10000)
    indice = models.CharField(max_length=10000)
    conclusion = models.CharField(max_length=10000)
    campus = models.ForeignKey('Campus',on_delete=models.SET_NULL,null=True)

    def __int__(self):
        return self.id

class DetalleAsignacion(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_autoguardado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10)
    documento = models.ForeignKey('Documento',on_delete=models.SET_NULL,null=True)
    usuario = models.ForeignKey('usuario.Usuario',on_delete=models.SET_NULL,null=True)

    def __int__(self):
        return self.id

class Capitulo(models.Model):
    nombre_capitulo = models.CharField(max_length=50)
    introduccion = models.CharField(max_length=10000)
    conclusion = models.CharField(max_length=10000)
    documento = models.ForeignKey(Documento, on_delete=models.SET_NULL, null=True)

    def __int__(self):
        return self.id

class Item(models.Model):
    parrafo = models.CharField(max_length=100000)
    nombre = models.CharField(max_length=50)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.SET_NULL, null=True)

    def __int__(self):
        return self.id

class Imagen(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField()
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class Observacion(models.Model):
    detalle = models.CharField(max_length=10000)
    fecha_observacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=50)
    documento = models.ForeignKey(Documento, on_delete=models.SET_NULL, null=True)

    def __int__(self):
        return self.id

class Anexo(models.Model):
    archivo = models.FileField()
    detalle = models.CharField(max_length=10000)
    fecha_ingreso = models.DateTimeField(auto_now=True)
    documento = models.ForeignKey(Documento, on_delete=models.SET_NULL, null=True)                             

    def __int__(self):
        return self.id

class Bibliografia(models.Model):
    autores = models.CharField(max_length=1000)
    nombre_publicacion = models.CharField(max_length=1000)
    fechas_publicacion= models.CharField(max_length=250)
    nombre_capitulo = models.CharField(max_length=700)
    num_pagina_incial = models.IntegerField()
    num_pagina_final = models.IntegerField()
    url_recurso = models.CharField(max_length=1500)
    documento = models.ForeignKey(Documento, on_delete=models.SET_NULL, null=True)

    def __int__(self):
        return self.id