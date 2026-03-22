[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)
# FOODTRUCK
Proyecto de Python orientado a objetos para gestionar la carta, los pedidos y los servicios de un food truck. Desarrollado como trabajo final de Programación II.

# FUNCIONAMIENTO DEL PROGRAMA
Simula el funcionamiento real de un food truck: puedes ver la carta con los productos disponibles, hacer pedidos de clientes, controlar el stock automáticamente y consultar el estado del servicio según el horario del día.

# ESTRUCTURA DEL PROYECTO
trabajo-final-a1/
- `producto.py` — Clase abstracta base de todos los productos
- `bebida.py` — Hereda de Producto, aplica recargo por tamaño
- `comida.py` — Hereda de Producto, aplica IVA al precio
- `postre.py` — Hereda de Producto, descuento si no tiene gluten
- `horario.py` — Controla la apertura y cierre del servicio
- `servicio.py` — Gestiona si se puede atender según el horario
- `pedido.py` — Pedidos con líneas, confirmación y operadores
- `foodtruck.py` — Clase central: menú, pedidos y ventas
- `prueba.py` — Menú interactivo para probar el sistema
- `README.md` — Documentación del proyecto

# REQUISITOS
Solo es necesario tener Python 3, no es necesario instalar nada extra.

# COMO EJECUTARLO
Descarga todos los archivos en la misma carpeta y ejecuta "python test_proyecto.py"