from src.carrito.carrito import Carrito
from src.carrito.modelos import Producto

def test_debe_eliminar_producto_por_nombre():

    carrito = Carrito()

    producto = Producto("Mouse", 100, 1)

    carrito.productos.append(producto)

    carrito.eliminar_producto("Mouse")

    assert len(carrito.productos) == 0