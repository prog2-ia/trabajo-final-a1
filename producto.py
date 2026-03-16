class Producto:
    def __init__(self, nombre, precio, stock):
        if precio < 0:
            raise ValueError("Precio no valido")
        if stock < 0:
            raise ValueError("Stock no valido")

        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f'{self.nombre} — {self.precio:.2f}€  [stock: {self.stock}]'
    def __repr__(self):
        return f'(nombre={self.nombre}, precio={self.precio}, stock={self.stock})'

    #--------------------------------------
    # GESTIÓN DE STOCK
    #--------------------------------------

    def reponer_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("No se puede reponer una cantidad negativa")
        self.stock += cantidad

    def reducir_stock(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("No se puede reducir a un stock negativo")
        self.stock -= cantidad

#-------------------------------
# PRUEBA
#-------------------------------

hamburguesa=Producto('Hamburguesa',12.30, 120)
agua=Producto('Agua',1.20, 200)

print(hamburguesa)
print(agua)

hamburguesa.reponer_stock(100)
agua.reducir_stock(100)

print(hamburguesa)
print(agua)