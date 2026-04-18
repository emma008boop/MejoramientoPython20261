def id_generator():
    current_id = 1
    while True:
        yield current_id
        current_id += 1


obtener_id = id_generator()


class Usuario:
    def __init__(self, correo: str, contraseña):
        self.__correo = correo
        self.__contraseña = contraseña
        self.id = next(obtener_id)

    @property
    def correo(self):
        return self.__correo

    @property
    def contraseña(self):
        return self.contraseña
