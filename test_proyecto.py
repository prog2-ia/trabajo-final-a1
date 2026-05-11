from datetime import datetime, date

from entities.bebida import Bebida
from entities.comida import Comida
from entities.postre import Postre
from entities.foodtruck import FoodTruck
from entities.pedido import Pedido
from entities.horario import Horario
from entities.servicio import Servicio
from entities.servicio_evento import ServicioEvento
from entities.jornada import Jornada
from entities.cierre_servicio import CierreService


# CREAR PRODUCTOS

bebida = Bebida(
    "Coca Cola",
    2.0,
    20,
    500
)

comida = Comida(
    "Hamburguesa",
    8.5,
    10,
    15
)

postre = Postre(
    "Brownie",
    4.0,
    5,
    False
)

# CREAR FOODTRUCK

foodtruck = FoodTruck(
    "Street Food UA",
    "Alicante"
)

foodtruck.agregar_producto(bebida)
foodtruck.agregar_producto(comida)
foodtruck.agregar_producto(postre)

print("=== MENÚ ===")

for producto in foodtruck.menu:
    print(
        producto.nombre,
        "-",
        producto.precio_venta(),
        "€"
    )

# CREAR PEDIDO

pedido = Pedido("Juan")

pedido.agregar_linea(comida, 2)
pedido.agregar_linea(bebida, 1)
pedido.agregar_linea(postre, 1)

foodtruck.registrar_pedido(pedido)

print("\n=== PEDIDO ===")
print(pedido)

# HORARIO

horario = Horario(
    datetime(2026, 5, 10, 12, 0),
    datetime(2026, 5, 10, 22, 0)
)

# SERVICIO NORMAL

servicio = Servicio(horario)

print("\n=== SERVICIO ===")
print(servicio.atender(datetime.now()))

# SERVICIO EVENTO

evento = ServicioEvento(
    horario,
    "Festival UA",
    300
)

print("\n=== EVENTO ===")
print(evento)

# JORNADA

jornada = Jornada(
    foodtruck,
    date.today(),
    18
)

print("\n=== JORNADA ===")
print(
    "Beneficio estimado:",
    jornada.beneficio_estimado,
    "€"
)

# CIERRE

cierre = CierreService(jornada)

print("\n=== CIERRE ===")
print(cierre.generar_resumen())

# FOODTRUCK

print("\n=== FOODTRUCK ===")
print(foodtruck)