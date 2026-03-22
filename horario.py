class Horario:
    'Clase que representa el horario de apertura '
    'No depende de nada'

    def __init__(self, hora_apertura: int, hora_cierre: int):
        if not (0 <= hora_apertura <= 23):
            raise ValueError("La hora de apertura debe estar entre 0 y 23")
        if not (0 <= hora_cierre <= 23):
            raise ValueError("La hora de cierre debe estar entre 0 y 23")
        if hora_cierre <= hora_apertura:
            raise ValueError("La hora de cierre debe ser mayor que la de apertura")

        self.__hora_apertura = hora_apertura
        self.__hora_cierre = hora_cierre

        # -------------------------
        # GETTERS DE LOS ATRIBUTOS PRIVADOS
        # -------------------------

    @property
    def hora_apertura(self) -> int:
        return self.__hora_apertura

    @property
    def hora_cierre(self) -> int:
        return self.__hora_cierre

        # -------------------------
        # MÉTODOS
        # -------------------------

    def esta_abierto(self, hora_actual: int) -> bool:
        """Devuelve True si el negocio está abierto en la hora indicada"""
        if not (0 <= hora_actual <= 23):
            raise ValueError("La hora actual debe estar entre 0 y 23")

        return self.__hora_apertura <= hora_actual < self.__hora_cierre

    def __str__(self):
        return f"Abierto de {self.__hora_apertura}:00 a {self.__hora_cierre}:00"


