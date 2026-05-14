"""
Pruebas del requerimiento RF3:
Calcular el total del carrito.
"""
from src.carrito.carrito import Carrito
from src.carrito.modelos import Producto


def test_debe_calcular_total_del_carrito():

    carrito = Carrito()

    producto1 = Producto("Teclado", 200, 2)
    producto2 = Producto("Mouse", 100, 1)

    carrito.productos.append(producto1)
    carrito.productos.append(producto2)

    total = carrito.calcular_total()

    assert total == 500
