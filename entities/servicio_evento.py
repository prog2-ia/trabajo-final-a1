
from datetime import datetime
from entities.servicio import Servicio
from entities.horario import Horario


class ServicioEvento(Servicio):
    """Servicio especial para eventos concretos."""

    def __init__(self, horario: Horario, nombre_evento: str, aforo_estimado: int):
        super().__init__(horario)

        if not nombre_evento.strip():
            raise ValueError("El nombre del evento no puede estar vacío.")

        if aforo_estimado <= 0:
            raise ValueError("El aforo estimado debe ser positivo.")

        self.__nombre_evento = nombre_evento.strip()
        self.__aforo_estimado = aforo_estimado

    # GETTERS
    @property
    def nombre_evento(self) -> str:
        return self.__nombre_evento

    @property
    def aforo_estimado(self) -> int:
        return self.__aforo_estimado

    # MÉTODOS
    def prioridad_servicio(self) -> str:
        if self.aforo_estimado >= 200:
            return "Alta"
        elif self.aforo_estimado >= 100:
            return "Media"
        return "Normal"

    def __str__(self) -> str:
        return (
            f"Evento: {self.nombre_evento} | "
            f"Aforo estimado: {self.aforo_estimado} personas"
        )

