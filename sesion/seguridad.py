import re

class Seguridad:

    def __init__(self):
        self.usuariosRegistrados = {}

    def correoValido(self, eMail):
        # Verificamos si el email cumple el formato RFC 822.
        if (re.match(r"[^@]+@[^@]+\.[^@]+", eMail) == None):
            return False
        
        return True	

    def usuarioYaRegistrado(self, eMail):
        if eMail in self.usuariosRegistrados:
            return True
        return False

    def coincidenClaves(self, claveUno, claveDos):
        # Verificamos si las claves coinciden.
        if(claveUno != claveDos):
            return False
        return True