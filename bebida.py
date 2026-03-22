from producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, mililitros: int) -> None:
        super().__init__(nombre, precio, stock)
        if mililitros <= 0:
            raise ValueError('Los mililitros deben ser positivos.')
        self.__mililitros = mililitros

    #------------------------------------
    # GETTERS DE LOS ATRIBUTOS PRIVADOS
    #------------------------------------
    @property
    def mililitros(self) -> int:
        return self.__mililitros
