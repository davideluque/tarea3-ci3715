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

    def testContrasenaInvalida(self):
        contrasenas_invalidas = ['1111111', # 7 Digitos
                                 '16161616161616161', # 17 Digitos
                                 'abu2y2353583782371', # 18 Digitos
                                 '9235580990k', # Falta mayuscula
                                 '9389235398K', # Falta minuscula
                                 '%zYzaaa1111'] # Tiene caracter especial
                                 
        for contrasena_invalida in contrasenas_invalidas:
            self.assertEqual(seguridad.validacionClave(contrasena_invalida), False)
            
    
    def testContrasenaValida(self):
        contrasenas_validas = ['MiClave123',
                               'contraseNa1',
                               'kk88Ymmm1',
                               'Password123',
                               'hjhadj7G']
        
        for contrasena_valida in contrasenas_validas:
            self.assertEqual(seguridad.validacionClave(contrasena_valida), True)