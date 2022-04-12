from django.test import TestCase
from rest_framework.test import APITestCase
from unittest import TestCase

class EtiquetasTestCase(APITestCase):
    def test_crear_etiqueta_success(self):
        self.assertEqual(1,1)