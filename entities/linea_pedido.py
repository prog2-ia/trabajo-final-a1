from dataclasses import dataclass
from entities.producto import Producto


@dataclass
class LineaPedido:
    producto: Producto
    cantidad: int

    def __post_init__(self) -> None:
        if self.cantidad <= 0:
            raise ValueError('La cantidad debe ser positiva.')

    @property
    def subtotal(self) -> float:
        return round(self.producto.precio_venta() * self.cantidad, 2)

