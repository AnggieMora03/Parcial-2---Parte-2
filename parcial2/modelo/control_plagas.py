from modelo.producto_control import ProductoControl
from modelo.errores import ValidationError

class ControlPlagas(ProductoControl):
    """
    Control de Plagas tiene periodo_carencia (dias).
    """
    def __init__(self, registro_ica: str, nombre: str, frecuencia_en_dias: int, precio: float, periodo_carencia_dias: int):
        super().__init__(registro_ica, nombre, frecuencia_en_dias, precio)
        if periodo_carencia_dias is None or not (isinstance(periodo_carencia_dias, int) and periodo_carencia_dias >= 0):
            raise ValidationError("periodo_carencia_dias es obligatorio y debe ser entero >= 0.")
        self.periodo_carencia_dias = int(periodo_carencia_dias)
