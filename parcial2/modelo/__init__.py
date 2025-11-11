#modelo/__init__.py
from .producto import Producto
from .producto_control import ProductoControl
from .control_plagas import ControlPlagas
from .fertilizante import Fertilizante
from .antibiotico import Antibiotico
from .cliente import Cliente
from .factura import Factura

__all__ = [
    "Producto", "ProductoControl", "ControlPlagas", "Fertilizante",
    "Antibiotico", "Cliente", "Factura"
]
