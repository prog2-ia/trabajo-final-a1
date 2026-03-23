from producto import Producto
'''
comida.py — Food Truck System
Clase: Comida  (hereda de Producto)

Representa cualquier plato sólido del menú:
entrantes, principales, postres y snacks '''

class Comida(Producto):
    CATEGORIAS_VALIDAS = {"entrante", "principal", "postre", "snack"}
    def __init__(self, nombre: str, precio_base: float, stock: int, minutos_preparacion: int):
        # Llamamos al __init__ de Producto
        super().__init__(nombre, precio_base, stock)
        # Validamos la categoría
        if minutos_preparacion <= 0:
            raise ValueError("Los minutos de preparación deben ser positivos.")
        self.__minutos_preparacion = minutos_preparacion

    # -------------------------
    # GETTER
    # -------------------------
    @property
    def minutos_preparacion(self) -> int:
        return self.__minutos_preparacion

    @property
    def categoria(self) -> str:
        return "Comida"

    def precio_venta(self) -> float:
        return round(self.precio_base * 1.18, 2)