from django.test import TestCase

from .seguridad import Seguridad
import unittest

seguridad = Seguridad()

class TestSeguridad(unittest.TestCase):

    def testCorreoValido(self):
        correos_validos = ['email@example.com',
                           'firstname.lastname@example.com'
                           'email@subdomain.example.com',
                           'firstname+lastname@example.com',
                           'email@123.123.123.123',
                           '1234567890@example.com',
                           'email@example-one.com']
        
        for correo_valido in correos_validos:
            self.assertEqual(seguridad.correoValido(correo_valido), True)
        
    def testCorreoInvalido(self):  
        correos_invalidos = ['plainaddress', 
                              '#@%^%#$@#$@#.com', 
                              '@example.com',
                              'email.example.com',
                              'email@example@example.com']

        for correo_invalido in correos_invalidos:
            self.assertEqual(seguridad.correoValido(correo_invalido), False)
