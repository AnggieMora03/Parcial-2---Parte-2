#modelo/producto_control.py
from datetime import timedelta
from modelo.producto import Producto
from modelo.errores import ValidationError

class ProductoControl(Producto):
    """
    Producto de Control (base para Fertilizantes y Control de Plagas).
    Atributos obligatorios: registro_ica, nombre, frecuencia_en_dias, precio
    """
    def __init__(self, registro_ica: str, nombre: str, frecuencia_en_dias: int, precio: float):
        if not registro_ica or not isinstance(registro_ica, str):
            raise ValidationError("registro_ica es obligatorio y debe ser cadena.")
        if frecuencia_en_dias is None or not (isinstance(frecuencia_en_dias, int) and frecuencia_en_dias > 0):
            raise ValidationError("frecuencia_en_dias es obligatoria y debe ser entero > 0.")
        super().__init__(nombre=nombre, precio=precio)
        self.registro_ica = registro_ica
        self.frecuencia_en_dias = int(frecuencia_en_dias)
