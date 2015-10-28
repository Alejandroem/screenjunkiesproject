from django.test import TestCase

# Create your tests here.
class screenjunkiesViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/registrarse/')
        self.assertEqual(resp.status_code,200)


"""class MyTest(TestCase):
    def Test_Forms(self):
        #Nombre, Telefono, Correo, Fecha Nacimiento, Direccion, Fecha Inicio de socio
        from_data  = {'Alejandro','55555555','alexalejandroem@gmail.com','16/3/2015','7av 11-14 A Zona 12','28/10/2015'}
"""