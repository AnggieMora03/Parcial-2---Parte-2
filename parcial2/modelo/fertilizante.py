#modelo/fertilizante.py
from datetime import date
from modelo.producto_control import ProductoControl
from modelo.errores import ValidationError

class Fertilizante(ProductoControl):
    """
    Fertilizante: además registra fecha_ultima_aplicacion (date).
    """
    def __init__(self, registro_ica: str, nombre: str, frecuencia_en_dias: int, precio: float, fecha_ultima_aplicacion: date):
        super().__init__(registro_ica, nombre, frecuencia_en_dias, precio)
        if fecha_ultima_aplicacion is None or not isinstance(fecha_ultima_aplicacion, date):
            raise ValidationError("fecha_ultima_aplicacion es obligatoria y debe ser datetime.date.")
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
