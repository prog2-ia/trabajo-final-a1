from entities.bebida import Bebida
from entities.comida import Comida
from entities.postre import Postre
from entities.pedido import Pedido
from entities.foodtruck import FoodTruck
from entities.horario import Horario
from entities.servicio import Servicio
from datetime import datetime

print("=" * 40)
print("   PRUEBA DEL FOOD TRUCK")
print("=" * 40)

truck = FoodTruck("FoodTruck de la UA", "San Vicente")

# Añadir productos al menú
truck.agregar_producto(Bebida("Limonada", 1.80, 10, 500))
truck.agregar_producto(Comida("Hamburguesa", 7.50, 8, 10))
truck.agregar_producto(Postre("Tarta de chocolate", 3.00, 6, True))

# Crear horario y servicio ---
horario = Horario(9, 22)
servicio = Servicio(horario)
hora_actual = datetime.now().hour

print("\n=== FOOD TRUCK MANAGER ===")
print(f"Horario: {horario}")
print(f"Estado ahora ({hora_actual}:00): {servicio.atender(hora_actual)}")

# --- Menú principal ---
opcion=""
while opcion !="5":
    print("\n=== FOOD TRUCK MANAGER ===")
    print("1. Ver menú")
    print("2. Hacer un pedido")
    print("3. Ver ventas totales")
    print("4. Ver estado del servicio")
    print("5. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        print("\n--- MENÚ ---")
        for p in truck.menu:
            print(f"{p}")

    elif opcion == "2":
        cliente = input("Nombre del cliente: ").strip()
        pedido = Pedido(cliente)
        while True:
            print("Productos disponibles:", ", ".join(p.nombre for p in truck.menu))
            nombre = input("Producto (o Enter para terminar): ").strip()
            if not nombre:
                break
            try:
                cantidad = int(input("Cantidad: ").strip())
                pedido.agregar_linea(truck.buscar_producto(nombre), cantidad)
                print("  Añadido.")
            except ValueError as e:
                print(f"  Error: {e}")
        try:
            truck.registrar_pedido(pedido)
            print(f"Pedido confirmado. Total: {pedido.total:.2f}€")
        except ValueError as e:
            print(f"  Error: {e}")

    elif opcion == "3":
        print(f"\nVentas totales: {truck.ventas_totales:.2f}€")

    elif opcion == "4":
        print(f"\n--- SERVICIO ---")
        print(f"  Horario: {horario}")
        print(f"  Hora actual: {hora_actual}:00")
        print(f"  Estado: {servicio.atender(hora_actual)}")

    elif opcion == "5":
        print("Hasta luego.")

    else:
        print("Opción no válida.")