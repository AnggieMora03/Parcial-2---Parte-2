#tests/test_producto_control.py
import pytest
from datetime import date
from modelo.control_plagas import ControlPlagas
from modelo.fertilizante import Fertilizante
from modelo.errores import ValidationError

def test_control_plagas_valido():
    cp = ControlPlagas("ICA-123", "Fungicida X", 30, 12000.0, periodo_carencia_dias=7)
    assert cp.registro_ica == "ICA-123"
    assert cp.periodo_carencia_dias == 7

def test_fertilizante_fecha_obligatoria():
    with pytest.raises(ValidationError):
        Fertilizante("ICA-2", "Fert A", 15, 5000.0, fecha_ultima_aplicacion=None)

def test_producto_control_frecuencia_invalida():
    with pytest.raises(ValidationError):
        ControlPlagas("ICA-3", "Producto", 0, 1000.0, periodo_carencia_dias=3)
