from producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio_base: float, stock: int, mililitros: int) -> None:
        super().__init__(nombre, precio_base, stock)
        if mililitros <= 0:
            raise ValueError("Los mililitros deben ser positivos.")
        self.__mililitros = mililitros

    #------------------------------------
    # GETTERS DE LOS ATRIBUTOS PRIVADOS
    #------------------------------------
    @property
    def mililitros(self) -> int:
        return self.__mililitros

    @property
    def categoria(self) -> str:
        return "Bebida"

    def precio_venta(self) -> float:
        if self.mililitros >= 400:
            recargo_frio = 0.35
        else:
            recargo_frio = 0.20
        return round(self.precio_base + recargo_frio, 2)
