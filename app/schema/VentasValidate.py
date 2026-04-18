from pydantic import BaseModel


class VentasValidate(BaseModel):
    id: int
    nombre_cliente: str
    numero_mesa: int
    plato_principal: str
    valor_consumo: float

    metodo_pago: str
    estado_pedido: str

    class Config:
        from_attributes = True
