import re

class Seguridad:

    def __init__(self):
        self.usuariosRegistrados = {}
        self.error_msg = ""

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

    def validacionClave(self, clave):
        # Verificamos la longitud de las claves.
        if(len(clave) < 8 or len(clave) > 16):
            self.error_msg = "Clave invalida, las claves deben tener entre 8 y 16 caracteres"
            return False			

        # Verificamos que no existan caracteres especiales en las claves.
        if not (clave.isalnum()):
            self.error_msg = "Clave invalida, las claves deben ser alfanumericas"
            return False

        # Verificamos que la clave tenga mas de dos letras, con al menos una mayuscula
        # y una minuscula.
        cantLetras = 0
        cantMay = 0
        for letra in clave:
            if (letra.isalpha()):
                cantLetras += 1
            if(letra.isupper()):
                cantMay += 1
        
        if not (cantLetras > 2 and cantMay > 0 and cantLetras - cantMay > 0):
            self.error_msg = "Clave invalida, la clave debe tener al menos tres letras, con al menos una mayuscula y una minuscula"
            return False

        # Verificamos que la clave contenga al menos un digito
        hayNum = False
        for letra in clave:
            if letra.isdigit():
                hayNum = True

        if not (hayNum):
            self.error_msg = "Clave invalida, la clave debe contener al menos un digito"
            return False

        return True
    
    def registrarUsuario(self, eMail, claveUno, claveDos):

        if not self.correoValido(eMail):
            return "Correo electronico invalido, no cumple con el formato RFC 822"

        if self.usuarioYaRegistrado(eMail):
            return "Usuario ya existe"

        if not self.coincidenClaves(claveUno, claveDos):
            return "Clave invalida, las claves deben coincidir"

        claveEsValida = self.validacionClave(claveUno)
        
        if claveEsValida:
            claveCodificada = claveUno[::-1]	
            self.usuariosRegistrados[eMail] = claveCodificada
            return True

        return self.error_msg

    def ingresarUsuario(self, eMail, clave):
        
        # Verificamos si el user existe
        userValido = False
        for mail in self.usuariosRegistrados:
            if(mail == eMail):
                userValido = True

        claveValida = False
        if(userValido and self.usuariosRegistrados[eMail] == clave[::-1]):
            claveValida = True  

        if not (userValido):
            return "Usuario invalido"
        elif not (claveValida):
            return "Clave invalida"
        if (userValido and claveValida):
            return True    