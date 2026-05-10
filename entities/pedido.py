from copy import deepcopy
from datetime import datetime

from entities.exceptions import PedidoInvalidoError
from entities.linea_pedido import LineaPedido

class Pedido:
    """Gestiona los de un pedido de un cliente."""

    def __init__(self, cliente: str, fecha: datetime | None = None) -> None:
        if not cliente.strip():
            raise ValueError('El cliente no puede estar vacío.')
        self.__cliente = cliente.strip()
        self.__fecha = fecha or datetime.now()
        self.__lineas: list[LineaPedido] = []

    # -------------------------
    # GETTER
    # -------------------------
    @property
    def cliente(self) -> str:
        return self.__cliente

    @property
    def lineas(self)-> list[LineaPedido]:
        return list(self.__lineas)

    @property
    def fecha(self) -> datetime:
        return self.__fecha

    # -------------------------
    # CONTROL LÍNEAS
    # -------------------------
    def agregar_linea(self, producto, cantidad: int) -> None:
        self.__lineas.append(LineaPedido(producto, cantidad))


    @property
    def total(self) -> float:
        return round(sum(linea.subtotal for linea in self.__lineas), 2)

    def confirmar(self) -> None:
        if not self.__lineas:
            raise PedidoInvalidoError('No se puede confirmar un pedido vacío.')
        for linea in self.__lineas:
            linea.producto.reducir_stock(linea.cantidad)

    def __add__(self, other: 'Pedido') -> 'Pedido':
        if not isinstance(other, Pedido):
            return NotImplemented
        if self.cliente != other.cliente:
            raise PedidoInvalidoError('Solo se pueden sumar pedidos del mismo cliente.')
        nuevo = Pedido(self.cliente, min(self.fecha, other.fecha))
        for linea in self.__lineas + other.__lineas:
            nuevo.__lineas.append(LineaPedido(linea.producto, linea.cantidad))
        return nuevo

    def __iadd__(self, other):
        if isinstance(other, LineaPedido):
            self.__lineas.append(other)
            return self
        if isinstance(other, Pedido):
            combinado = self + other
            self.__lineas = combinado.__lineas
            self.__fecha = combinado.__fecha
            return self
        return NotImplemented

    def __lt__(self, other: 'Pedido') -> bool:
        if not isinstance(other, Pedido):
            return NotImplemented
        return self.total < other.total

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pedido):
            return False
        return self.total == other.total

    def clonar(self) -> 'Pedido':
        return deepcopy(self)

    def __str__(self) -> str:
        return f'Pedido de {self.cliente} - {len(self.__lineas)} líneas - total {self.total:.2f} EUR'
