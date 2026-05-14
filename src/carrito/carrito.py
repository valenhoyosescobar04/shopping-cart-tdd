class Carrito:

    def __init__(self):
        self.productos = []

    def eliminar_producto(self, nombre):

        self.productos = [
            producto
            for producto in self.productos
            if producto.nombre != nombre
        ]

    def calcular_total(self):

        return sum(
            producto.calcular_subtotal()
            for producto in self.productos
        )