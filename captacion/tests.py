from django.test import TestCase
from .models import Tipo
from django.core.exceptions import ValidationError
# Create your tests here.
class TestTipo(TestCase):
    def test_grabacion(self):
        with self.assertRaises(ValidationError) as qv:
            q= Tipo.objects.create(nombre='Brangus')
            q.full_clean()

        mensaje_error = dict(qv.exception)
        self.assertEqual(mensaje_error["nombre"][0], "No es una opcion permitida")       
