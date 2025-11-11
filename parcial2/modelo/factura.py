#modelo/factura.py
from datetime import date
from typing import List
from modelo.errores import ValidationError
from modelo.producto import Producto

class Factura:
    """
    Factura (Pedido): fecha (date), productos (lista de Producto).
    El valor total se calcula sumando precios de productos.
    """
    def __init__(self, fecha: date, productos: List[Producto]):
        if fecha is None:
            raise ValidationError("fecha es obligatoria.")
        if not isinstance(productos, list) or len(productos) == 0:
            raise ValidationError("productos debe ser una lista no vacía de objetos Producto.")
        for p in productos:
            if not isinstance(p, Producto):
                raise ValidationError("Todos los elementos de productos deben heredar de Producto.")
        self.fecha = fecha
        self.productos = list(productos)

    def total(self) -> float:
        return sum(p.precio for p in self.productos)

    def agregar_producto(self, producto: Producto):
        if producto is None or not isinstance(producto, Producto):
            raise ValidationError("producto debe ser instancia de Producto.")
        self.productos.append(producto)
