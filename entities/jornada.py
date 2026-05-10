from datetime import date

from entities.foodtruck import FoodTruck


class Jornada:
    def __init__(self, food_truck: FoodTruck, fecha: date, combustible_gastado: float) -> None:
        if combustible_gastado < 0:
            raise ValueError('El combustible gastado no puede ser negativo.')
        self.__food_truck = food_truck
        self.__fecha = fecha
        self.__combustible_gastado = float(combustible_gastado)

    @property
    def food_truck(self) -> FoodTruck:
        return self.__food_truck

    @property
    def fecha(self) -> date:
        return self.__fecha

    @property
    def combustible_gastado(self) -> float:
        return self.__combustible_gastado

    @property
    def beneficio_estimado(self) -> float:
        coste_combustible = self.combustible_gastado * 1.65
        return round(self.food_truck.ventas_totales - coste_combustible, 2)

