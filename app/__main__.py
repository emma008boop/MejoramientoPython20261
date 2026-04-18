from app.schema.UsuarioValidate import UsuarioValidate
from app.schema.VentasValidate import VentasValidate
from app.service.UsuarioService import UsuarioService
from app.service.VentaService import VentaService


def menu_ventas():
    servicio = VentaService()
    while True:
        print("\n   SISTEMA DE VENTAS")
        print("1. Mostrar todas las ventas")
        print("2. Ordenar por valor (Menor a Mayor)")
        print("3. Buscar venta por ID")
        print("4. Eliminar una venta")
        print("5. Agregar una nueva venta")
        print("0. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            servicio.mostrar_ventas()
        elif opcion == "2":
            servicio.ordenar_por_valor()
            print("Ventas ordenadas correctamente.")
        elif opcion == "3":
            try:
                id_b = int(input("ID de la venta: "))
                v = servicio.buscar_por_id(id_b)
                print(v if v else "No encontrada.")
            except ValueError:
                print("ID inválido.")
        elif opcion == "4":
            try:
                id_e = int(input("ID a eliminar: "))
                print(servicio.eliminar_venta(id_e))
            except ValueError:
                print("ID inválido.")
        elif opcion == "5":
            try:
                id_v = int(input("Id: "))
                nom = input("Cliente: ")
                mes = int(input("Mesa: "))
                pla = input("Plato: ")
                val = float(input("Valor: "))
                pag = input("Método: ").upper()

                datos_v = VentasValidate(
                    id=id_v,
                    nombre_cliente=nom,
                    numero_mesa=mes,
                    plato_principal=pla,
                    valor_consumo=val,
                    metodo_pago=pag,
                    estado_pedido="PENDIENTE",
                )
                print(servicio.agregar_venta(datos_v))
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "0":
            break


def menu_usuario():
    servicio = UsuarioService()
    while True:
        print("\n   SISTEMA DE USUARIOS   ")
        print("1. Registrarse")
        print("2. Logueo")
        print("3. Salir")

        opcion = input("\n Seleccione una opcion: ")

        if opcion == "1":
            try:
                u_name = input("Nombre de usuario: ")
                u_pass = input("Contraseña: ")
                u_mail = input("Email: ")

                datos_reg = UsuarioValidate(
                    username=u_name, contraseña=u_pass, correo=u_mail
                )
                print(servicio.registrar(datos_reg))
            except Exception as e:
                print(f"Error de registro: {e}")

        elif opcion == "2":
            try:
                # Cambiamos 'Usuario' por 'Email' para el login
                email_login = input("Email: ")
                pass_login = input("Contraseña: ")

                # Para el login, enviamos un username genérico si el esquema lo pide,
                # pero usamos el email real ingresado.
                datos_log = UsuarioValidate(
                    username="usuario_login", contraseña=pass_login, correo=email_login
                )

                if servicio.login(datos_log):
                    print("\n--- ACCESO CONCEDIDO ---")
                    while True:
                        print("\n1. Gestionar ventas")
                        print("2. Cerrar Sesión")
                        op = input("\n Seleccione: ")
                        if op == "1":
                            menu_ventas()
                        elif op == "2":
                            break
                else:
                    print("Credenciales incorrectas.")
            except Exception as e:
                print(f"Error de formato: {e}")

        elif opcion == "3":
            break


if __name__ == "__main__":
    menu_usuario()
