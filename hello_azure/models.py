from django.db import models

class MisDatos(models.Model):
    nombre = models.CharField(max_length=255, null=True)
    correo = models.CharField(max_length=60, null=True)
    telefono = models.CharField(max_length=15, null=True)
    empresa = models.CharField(max_length=255, null=True)
    codigo = models.CharField(max_length=15, null=True)
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    estado = models.CharField(max_length=2, null=True)
    joined_date = models.DateField(null=True)
    
class MisCursos(models.Model):
    usuario = models.CharField(max_length=15)
    cursos = models.CharField(max_length=255, null=True)
    certificado = models.CharField(max_length=2, null=True)