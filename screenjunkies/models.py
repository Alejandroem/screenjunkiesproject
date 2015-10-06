from django.db import models
from django.core.validators import *
# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=200, validators=[RegexValidator(r'^[a-zA-Z\' \']*$', 'El nombre solo permite letras de A-Z')])
    telefono = models.IntegerField(validators=[MaxValueValidator(99999999),MinValueValidator(10000000)])
    correoElectronico = models.EmailField()
    fechaNacimiento = models.DateTimeField()
    direccionDomicilio = models.CharField(max_length=200, validators=[RegexValidator(r'^[0-9a-zA-Z\'\-\'\' \']*$', 'La dirreccion no permite simbolos extranios')])
    fechaInicioSocio = models.DateTimeField()

    def __unicode__(self):
        return self.Nombre

    class Meta:
        db_table = 'Usuario'


