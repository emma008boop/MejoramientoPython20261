import pandas as pd

from app.data.data import ventas_restaurante
from app.model.Venta import Venta
from app.schema.VentasValidate import VentasValidate


class VentaService:
    def __init__(self):
        self.__ventas = [
            Venta(
                id=v["idVenta"],
                nombre_cliente=v["nombreCliente"],
                numero_mesa=v["numeroMesa"],
                plato_principal=v["platoPrincipal"],
                valor_consumo=v["valorConsumo"],
                metodo_pago=v["metodoPago"],
                estado_pedido=v["estadoPedido"],
            )
            for v in ventas_restaurante
        ]

    @property
    def ventas(self):
        return self.__ventas

    @property
    def id(self):
        return self.__id

    def mostrar_ventas(self):
        for v in self.__ventas:
            print(
                f"ID: {v.id} | Cliente: {v.nombre_cliente} | Total: ${v.valor_consumo}"
            )

    def ordenar_por_valor(self):
        data_para_df = [
            {"id": v.id, "cliente": v.nombre_cliente, "valor_consumo": v.valor_consumo}
            for v in self.ventas
        ]

        df = pd.DataFrame(data_para_df)

        df_ordenado = df.sort_values(by="valor_consumo", ascending=True)

        print(df_ordenado)

    def buscar_ventas_por_id(self, id: int):
        for v in self.ventas:
            if v.id == id:
                print(
                    f"ID: {v.id} \n Cliente: {v.nombre_cliente} \n Mesa: {v.numero_mesa} \n Plato principal: {v.plato_principal} \n Valor: {v.valor_consumo} Metodo de pago: {v.metodo_pago} \n Estado del pedido: {v.estado_pedido}"
                )
                return v
        return None

    def eliminar_venta(self, id: int):
        venta = self.buscar_ventas_por_id(id=id)
        if venta:
            self.__ventas.remove(venta)
            return f"Venta con id: {id} fue eliminada"
        return "Venta no encontrada"

    def agregar_venta(self, datos: VentasValidate):
        nueva_venta = Venta(
            id=datos.id,
            nombre_cliente=datos.nombre_cliente,
            numero_mesa=datos.numero_mesa,
            plato_principal=datos.plato_principal,
            valor_consumo=datos.valor_consumo,
            metodo_pago=datos.metodo_pago,
            estado_pedido=datos.estado_pedido,
        )
        self.__ventas.append(nueva_venta)
        return f"Venta #{datos.id} agregada correctamente"
