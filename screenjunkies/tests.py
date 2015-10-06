from django.test import TestCase
from django.utils import timezone
from screenjunkies.models import *
from screenjunkies.forms import *

# Create your tests here.
#viewtest
class screenjunkiesViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/registrarse/')
        self.assertEqual(resp.status_code, 200)

#modeltest
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

#formtest
class screenjunkiesFormsTestCase(TestCase):
    def test_informacion_valida(self):
        a = timezone.now()
        data = {
            'Nombre':'Prueba',
           'telefono':'55555555',
           'correoElectronico':'alexalejandro123@gmail.com',
           'fechaNacimiento':a,
           'direccionDomicilio':'7av 16-16 A Zona 15',
           'fechaInicioSocio':a,
        }
        form = UsuarioForm(data)
        self.assertTrue(form.is_valid())
        usuario = form.save()
        self.assertEqual(usuario.Nombre, "Prueba")
        self.assertEqual(usuario.telefono,55555555)
        self.assertEqual(usuario.correoElectronico, "alexalejandro123@gmail.com")
        self.assertEqual(usuario.fechaNacimiento,a)
        self.assertEqual(usuario.direccionDomicilio, "7av 16-16 A Zona 15")
        self.assertEqual(usuario.fechaInicioSocio,a)

    def test_informacion_vacia(self):
        form = UsuarioForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors,{
            'Nombre':[u'This field is required.'],
            'telefono':[u'This field is required.'],
            'correoElectronico':[u'This field is required.'],
            'fechaNacimiento':[u'This field is required.'],
            'direccionDomicilio':[u'This field is required.'],
            'fechaInicioSocio':[u'This field is required.'],
        })