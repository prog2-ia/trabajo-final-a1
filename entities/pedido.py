class Pedido:
    """Gestiona las líneas de un pedido de un cliente."""

    def __init__(self, cliente: str):
        if not cliente.strip():
            raise ValueError("El cliente no puede estar vacío.")
        self.__cliente = cliente.strip()
        self.__lineas = []  # lista de (producto, cantidad)

    # -------------------------
    # GETTER
    # -------------------------
    @property
    def cliente(self) -> str:
        return self.__cliente

    @property
    def lineas(self):
        return list(self.__lineas)

    # -------------------------
    # CONTROL LÍNEAS
    # -------------------------
    def agregar_linea(self, producto, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        self.__lineas.append((producto, cantidad))

    @property
    def total(self) -> float:
        return round(sum(p.precio_venta() * c for p, c in self.__lineas), 2)

    def confirmar(self):
        """Descuenta el stock de cada producto al confirmar el pedido."""
        if not self.__lineas:
            raise ValueError("No se puede confirmar un pedido vacío.")
        for producto, cantidad in self.__lineas:
            producto.reducir_stock(cantidad)


    def __str__(self):
        return f"Pedido de {self.__cliente} — total: {self.total:.2f}€"