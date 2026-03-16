from producto import Producto
'''
comida.py — Food Truck System
Clase: Comida  (hereda de Producto)

Representa cualquier plato sólido del menú:
entrantes, principales, postres y snacks '''

class Comida(Producto):
    CATEGORIAS_VALIDAS = {"entrante", "principal", "postre", "snack"}
    def __init__(self, nombre: str, precio: float, stock: int,
                 categoria: str, tiempo_prep: int):
        # Llamamos al __init__ del padre (Producto)
        super().__init__(nombre, precio, stock)
        # Validamos la categoría
        categoria = categoria.lower()
        if categoria not in self.CATEGORIAS_VALIDAS:
            raise ValueError(
                f"Categoría '{categoria}' no válida. "
                f"Opciones: {self.CATEGORIAS_VALIDAS}"
            )
            #Validamos el tiempo de preparación
            if tiempo_prep < 0:
                raise ValueError("El tiempo de preparación no puede ser negativo.")

            self._categoria = categoria
            self._tiempo_prep = tiempo_prep  # en minutos

