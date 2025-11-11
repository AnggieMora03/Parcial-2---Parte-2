#tests/test_factura_cliente.py
from datetime import date
import pytest
from modelo.antibiotico import Antibiotico
from modelo.fertilizante import Fertilizante
from modelo.factura import Factura
from modelo.cliente import Cliente
from modelo.errores import ValidationError

def test_factura_total_y_historial():
    a = Antibiotico("Antibio A", 500, "Porcinos", 20000.0)
    f = Fertilizante("ICA-9", "Fert B", 30, 15000.0, fecha_ultima_aplicacion=date(2025,1,1))
    factura = Factura(date.today(), [a, f])
    assert factura.total() == 35000.0

    cliente = Cliente("Juan", "12345678")
    cliente.agregar_factura(factura)
    assert cliente.total_gastado() == 35000.0

def test_factura_productos_vacio():
    with pytest.raises(ValidationError):
        Factura(date.today(), [])
