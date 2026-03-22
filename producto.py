from abc import ABC, abstractmethod

class Producto(ABC):
    """"CLASE ABSTRACTA | PRODUCTO BASE DEL MENU DEL FOOD TRUCK"""

    def __init__(self, nombre: str, precio: float, stock: int):
        if precio <= 0:
            raise ValueError("Precio no valido")
        if stock < 0:
            raise ValueError("Stock no valido")

        self.__nombre = nombre
        self.__precio = float(precio)
        self.__stock = stock

    #------------------------------------
    # GETTERS DE LOS ATRIBUTOS PRIVADOS
    #------------------------------------
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def precio_base(self) -> float:
        return self.__precio

    @property
    def stock(self) -> int:
        return self.__stock

    #--------------------------------------
    # GESTIÓN DE STOCK
    #--------------------------------------
    def reponer_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("No se puede reponer una cantidad negativa")
        self.__stock += cantidad

    def reducir_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError('La cantidad a descontar debe ser positiva')
        if cantidad > self.__stock:
            raise ValueError("No se puede reducir a un stock negativo")
        self.__stock -= cantidad

    #--------------------------------------
    # MÉTODOS ESPECIALES
    #--------------------------------------
    def __str__(self):
        return f'{self.__nombre} — {self.__precio:.2f}€  [stock: {self.__stock}]'
    def __repr__(self):
        return f'(nombre={self.__nombre}, precio={self.__precio}, stock={self.__stock})'
