class Venta:
    def __init__(
        self,
        id: int,
        nombre_cliente: str,
        numero_mesa: int,
        plato_principal: str,
        valor_consumo: float,
        metodo_pago: str,
        estado_pedido: str,
    ):
        self.__id = id
        self.__nombre_cliente = nombre_cliente
        self.__numero_mesa = numero_mesa
        self.__plato_principal = plato_principal
        self.__valor_consumo = valor_consumo
        self.__metodo_pago = metodo_pago
        self.__estado_pedido = estado_pedido

    @property
    def id(self):
        return self.__id

    @property
    def nombre_cliente(self):
        return self.__nombre_cliente

    @property
    def numero_mesa(self):
        return self.__numero_mesa

    @property
    def plato_principal(self):
        return self.__plato_principal

    @property
    def valor_consumo(self):
        return self.__valor_consumo

    @property
    def metodo_pago(self):
        return self.__metodo_pago

    @property
    def estado_pedido(self):
        return self.__estado_pedido
