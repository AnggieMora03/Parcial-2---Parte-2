#modelo/cliente.py
from typing import List
from modelo.errores import ValidationError
from modelo.factura import Factura

class Cliente:
    """
    Cliente habitual: nombre, cedula (obligatorios). Mantiene historial de Facturas.
    """
    def __init__(self, nombre: str, cedula: str):
        if not nombre or not isinstance(nombre, str):
            raise ValidationError("nombre es obligatorio y debe ser cadena.")
        if not cedula or not isinstance(cedula, str):
            raise ValidationError("cedula es obligatorio y debe ser cadena.")
        self.nombre = nombre
        self.cedula = cedula
        self.historial: List[Factura] = []

    def agregar_factura(self, factura: 'Factura'):
        if factura is None:
            raise ValidationError("factura no puede ser None.")
        self.historial.append(factura)

    def total_gastado(self) -> float:
        return sum(f.total() for f in self.historial)

    #obtener todas las facturas
    def obtener_facturas(self) -> List[Factura]:
        return list(self.historial)

    # obtener todos los productos comprados
    def obtener_productos_comprados(self):
        productos = []
        for factura in self.historial:
            productos.extend(factura.productos)
        return productos
