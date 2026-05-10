from producto import Producto
from pedido import Pedido


class FoodTruck:
    """Clase central que gestiona el menú y los pedidos del food truck."""

    def __init__(self, nombre: str, ciudad: str):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()
        self.__ciudad = ciudad.strip()
        self.__menu = []
        self.__pedidos = []

    # -------------------------
    # GETTER
    # -------------------------
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def ciudad(self) -> str:
        return self.__ciudad

    @property
    def menu(self):
        return list(self.__menu)

    @property
    def pedidos(self):
        return list(self.__pedidos)


    def agregar_producto(self, producto: Producto):
        self.__menu.append(producto)

    def buscar_producto(self, nombre: str) -> Producto:
        for p in self.__menu:
            if p.nombre.lower() == nombre.lower():
                return p
        raise ValueError(f"No existe el producto {nombre}.")

    def registrar_pedido(self, pedido: Pedido):
        pedido.confirmar()
        self.__pedidos.append(pedido)

    @property
    def ventas_totales(self) -> float:
        return round(sum(p.total for p in self.__pedidos), 2)

    def __str__(self):
        return f"{self.__nombre} ({self.__ciudad}) — ventas: {self.ventas_totales:.2f}€"