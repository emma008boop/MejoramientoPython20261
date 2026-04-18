from app.service.UsuarioService import UsuarioService
from app.service.VentaService import VentaService


def menu_ventas():
    servicio = VentaService()

    while True:
        print("   SISTEMA DE VENTAS")
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
            id_buscada = int(input("Ingresa el ID de la venta: "))
            venta = servicio.buscar_por_id(id_buscada)
            print(venta if venta else "Venta no encontrada.")

        elif opcion == "4":
            id_eliminar = int(input("Ingresa el ID a eliminar: "))
            mensaje = servicio.eliminar_venta(id_eliminar)
            print(mensaje)

        elif opcion == "5":
            id = input("Id de la venta: ")
            nombre = input("Nombre cliente: ")
            mesa = int(input("Mesa: "))
            plato = input("Plato principal: ")
            valor = float(input("Valor consumo: "))
            pago = input("Método (EFECTIVO/TARJETA/TRANSFERENCIA): ").upper()

            mensaje = servicio.agregar_venta(id, nombre, mesa, plato, valor, pago)
            print(mensaje)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


def menu_usuario():
    servicio = UsuarioService()
    while True:
        print("   Registro   ")
        print("1. Registrarse")
        print("2. Logueo")
        print("3. Salir")

        opcion = input("\n Seleccione una opcion: ")
        if opcion == "1":
            servicio.registrar()
        elif opcion == "2":
            servicio.login()
            print("1. Gestionar ventas del restaurante")
            print("2. Salir")
            while True:
                ver_menu_ventas = input("\n Seleccione una opcion")
                if ver_menu_ventas == "1":
                    menu_ventas()
                elif ver_menu_ventas == "2":
                    print("Saliendo")
                    break
                else:
                    print("Opcion no valida")
        elif opcion == "3":
            print("Saliendo del sistema.")
            break


menu_usuario()
