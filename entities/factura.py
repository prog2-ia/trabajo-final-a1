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

        # GETTERS

    @property
    def fecha(self):
        return self.__fecha

    @property
    def cliente(self):
        return self.__pedido.cliente

    @property
    def total(self):
        return self.__pedido.total

        # MÉTODOS

    def generar_factura(self) -> str:
        """Genera la factura en formato texto"""
        resultado = "FACTURA=\n"
        resultado += f"Cliente: {self.cliente}\n"
        resultado += f"Fecha: {self.__fecha.strftime('%d/%m/%Y %H:%M')}\n\n"

        resultado += "Productos:\n"
        for producto, cantidad in self.__pedido.lineas:
            resultado += f"- {producto.nombre} x{cantidad} → {producto.precio_venta()}€\n"

        resultado += f"TOTAL: {self.total:.2f}€\n"
        return resultado

    def __str__(self):
        return self.generar_factura()