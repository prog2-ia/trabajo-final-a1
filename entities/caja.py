class Caja:
    """Gestiona el dinero del food truck"""

    def __init__(self):
        self.__saldo = 0.0

    # GETTER
    @property
    def saldo(self) -> float:
        return self.__saldo

    # MÉTODOS
    def registrar_ingreso(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__saldo += cantidad

    def registrar_pedido(self, pedido):
        """Añade el dinero de un pedido a la caja"""
        self.registrar_ingreso(pedido.total)

    def reiniciar_caja(self):
        """Reinicia el saldo (ej: fin de día)"""
        self.__saldo = 0.0

    def __str__(self):
        return f"Caja actual: {self.__saldo:.2f}€"