from entities.foodtruck import FoodTruck
from entities.jornada import Jornada


class CierreService:
    """Gestiona el cierre diario del food truck."""

    def __init__(self, jornada: Jornada):
        self.__jornada = jornada

    # GETTERS
    @property
    def jornada(self) -> Jornada:
        return self.__jornada

    # MÉTODOS

    def resumen_ventas(self) -> str:
        return (
            f"Ventas totales: "
            f"{self.jornada.food_truck.ventas_totales:.2f}€"
        )

    def beneficio_final(self) -> float:
        return self.jornada.beneficio_estimado

    def generar_resumen(self) -> str:
        return (
            f"--- CIERRE DE JORNADA ---\n"
            f"FoodTruck: {self.jornada.food_truck.nombre}\n"
            f"Fecha: {self.jornada.fecha}\n"
            f"Ventas: {self.jornada.food_truck.ventas_totales:.2f}€\n"
            f"Beneficio estimado: {self.beneficio_final():.2f}€"
        )