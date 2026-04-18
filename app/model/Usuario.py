class Usuario:
    def __init__(self, correo: str, contraseña):
        self.__correo = correo
        self.__contraseña = contraseña

    @property
    def correo(self):
        return self.__correo

    @property
    def contraseña(self):
        return self.contraseña
