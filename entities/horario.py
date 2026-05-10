
from datetime import datetime, timedelta

class Horario:
    'Clase que representa el horario de apertura '

    def __init__(self, inicio: datetime, fin: datetime) -> None:
        if fin <= inicio:
            raise ValueError('La hora de fin debe ser posterior al inicio.')
        self.__inicio = inicio
        self.__fin = fin


    #------------------------------------
    # GETTERS DE LOS ATRIBUTOS PRIVADOS
    #------------------------------------
    @property
    def inicio(self) -> datetime:
        return self.__inicio

    @property
    def fin(self) -> datetime:
        return self.__fin

    @property
    def duracion_minutos(self) -> int:
        return int((self.fin - self.inicio).total_seconds() // 60)

    def contiene(self, otro: 'Horario') -> bool:
        return self.inicio <= otro.inicio and otro.fin <= self.fin

    def desplazar(self, minutos: int) -> 'Horario':
        return Horario(self.inicio + timedelta(minutes=minutos), self.fin + timedelta(minutes=minutos))

    def __str__(self) -> str:
        return f'{self.inicio:%d/%m/%Y %H:%M} - {self.fin:%H:%M}'



