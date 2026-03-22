from producto import Producto


class Postre(Producto):
    def __init__(self, nombre: str, precio_base: float, stock: int, tiene_gluten: bool):
        super().__init__(nombre, precio_base, stock)
        self.__tiene_gluten = bool(tiene_gluten)


    #------------------------------------
    # GETTERS DE LOS ATRIBUTOS PRIVADOS
    #------------------------------------

    @property
    def tiene_gluten(self) -> bool:
        return self.__tiene_gluten
