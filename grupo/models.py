from django.db import models
from ckeditor.fields import RichTextField

class Banda(models.Model):
    nombre = models.CharField(max_length=30)
    cant_integrantes = models.IntegerField()
    descripcion = RichTextField(null=True)
    
    
    
