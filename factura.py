from datetime import datetime
from pedido import Pedido


class Factura:
    """Representa la factura asociada a un pedido"""

    def __init__(self, pedido: Pedido):
        if not isinstance(pedido, Pedido):
            raise TypeError("Se debe proporcionar un objeto Pedido")

        if not pedido.lineas:
            raise ValueError("No se puede generar una factura de un pedido vacío")

        self.__pedido = pedido
        self.__fecha = datetime.now()