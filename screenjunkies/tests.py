from django.test import TestCase
from django.utils import timezone
from screenjunkies.models import *


# Create your tests here.
class screenjunkiesViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/registrarse/')
        self.assertEqual(resp.status_code, 200)


class screenjunkiesModelUsuarioTestCase(TestCase):
    def crear_usuario(self, nombre="Alejandro"
                      , telefono="55555555"
                      , correoElectronico="alexalejandro123@gmail.com"
                      , fechaNacimiento=timezone.now()
                      , direccionDomicilio="7av 16-16 A Zona 15"
                      , fechaInicioSocio=timezone.now()
                      ):
        return Usuario.objects.create(Nombre=nombre
                                      , telefono=telefono
                                      , correoElectronico=correoElectronico
                                      , fechaNacimiento=fechaNacimiento
                                      , direccionDomicilio=direccionDomicilio
                                      , fechaInicioSocio=fechaInicioSocio)

    def test_crear_usuario(self):
        u = self.crear_usuario()
        self.assertTrue(isinstance(u, Usuario))
        self.assertEqual(u.__unicode__(), u.Nombre)
