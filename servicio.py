from horario import Horario


class Servicio:
    """Clase que gestiona el servicio del food truck según su horario"""

    def __init__(self, horario: Horario):
        if not isinstance(horario, Horario):
            raise TypeError("Se debe proporcionar un objeto Horario")

        self.__horario = horario

    # -------------------------
    # GETTER
    # -------------------------
    @property
    def horario(self):
        return self.__horario

    # -------------------------
    # MÉTODOS
    # -------------------------
    def esta_abierto(self, hora_actual: int):
        """Devuelve si el servicio está disponible"""
        return self.__horario.esta_abierto(hora_actual)

    def atender(self, hora_actual: int):
        """Simula si se puede atender a un cliente"""
        if self.esta_abierto(hora_actual):
            return "Servicio disponible. Se puede atender al cliente."
        else:
            return "Servicio cerrado. No se puede atender."