from entities.servicio_ruta import ServicioRuta
from entities.servicio_evento import ServicioEvento
from entities.servicio_mixto import ServicioMixto


class PlanificacionService:
    """Gestiona la planificación de servicios del food truck."""

    def __init__(self):
        self.__servicios = []

    @property
    def servicios(self):
        return list(self.__servicios)

    # -------------------------
    # MÉTODOS
    # -------------------------
    def agregar_servicio(self, servicio):
        if not isinstance(
                servicio,
                (ServicioRuta, ServicioEvento, ServicioMixto)
        ):
            raise TypeError("Tipo de servicio no válido.")

        self.__servicios.append(servicio)

    def total_servicios(self) -> int:
        return len(self.__servicios)

    def servicios_evento(self):
        return [
            servicio
            for servicio in self.__servicios
            if isinstance(servicio, ServicioEvento)
        ]

    def servicios_ruta(self):
        return [
            servicio
            for servicio in self.__servicios
            if isinstance(servicio, ServicioRuta)
        ]