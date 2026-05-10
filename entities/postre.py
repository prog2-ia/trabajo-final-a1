from entities.producto import Producto


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

    @property
    def categoria(self) -> str:
        return 'Postre'

    def precio_venta(self) -> float:
        if not self.tiene_gluten:
            descuento_artesanal = 0.15
        else:
            descuento_artesanal = 0
        return round(self.precio_base * 1.12 + descuento_artesanal, 2)

