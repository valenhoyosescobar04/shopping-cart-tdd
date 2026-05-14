class Carrito:

    def __init__(self):
        self.productos = []

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del carrito usando su nombre.
        """

        self.productos = [
            producto
            for producto in self.productos
            if producto.nombre != nombre
        ]