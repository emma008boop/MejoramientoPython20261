from app.model.Usuario import Usuario
from app.schema.UsuarioValidate import UsuarioValidate


class UsuarioService:
    def __init__(self):
        self.usuarios_registrados = []

    def registrar(self, datos: UsuarioValidate):
        nuevo_usuario = Usuario(datos.correo, datos.contraseña)
        self.usuarios_registrados.append(nuevo_usuario)
        print(f"Usuario con email: {datos.correo}. Creado")
        return True

    def login(self, datos: UsuarioValidate):
        intentos = 4
        for u in self.usuarios_registrados:
            if u.correo == datos.correo:
                usuario_encontrado = u
                break
        if not usuario_encontrado:
            return f"Correo {datos.correo} no existe"
        intentos = 4
        if usuario_encontrado.contraseña == datos.contraseña:
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
                datos.contraseña = input("Introduce la contraseña de nuevo")
            else:
                return "Cuenta bloqueada temporalmente"
