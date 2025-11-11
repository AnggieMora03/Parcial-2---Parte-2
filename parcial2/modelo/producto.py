#modelo/producto.py
from abc import ABC, abstractmethod
from modelo.errores import ValidationError

class Producto(ABC):
    """Clase abstracta para cualquier producto de la tienda."""
    @abstractmethod
    def __init__(self, nombre: str, precio: float):
        if not nombre or not isinstance(nombre, str):
            raise ValidationError("nombre es obligatorio y debe ser cadena.")
        if precio is None or not (isinstance(precio, (int, float)) and precio >= 0):
            raise ValidationError("precio es obligatorio y debe ser numérico >= 0.")
        self.nombre = nombre
        self.precio = float(precio)

    def __repr__(self):
        return f"<{self.__class__.__name__} nombre={self.nombre} precio={self.precio}>"
