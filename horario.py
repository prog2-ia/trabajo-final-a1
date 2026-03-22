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

