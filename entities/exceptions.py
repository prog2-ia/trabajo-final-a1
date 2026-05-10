class FoodTruckError(Exception):
    """Base de excepciones del dominio."""

class StockInsuficienteError(FoodTruckError):
    """Cuando no hay stock suficiente para servir un pedido."""

class TiempoInalcanzableError(FoodTruckError):
    """Cuando una ruta o evento no cabe dentro del horario disponible."""

class PedidoInvalidoError(FoodTruckError):
    """Cuando un pedido no cumple las reglas de negocio."""

