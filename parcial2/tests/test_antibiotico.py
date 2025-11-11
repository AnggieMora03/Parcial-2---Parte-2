#tests/test_antibiotico.py
import pytest
from modelo.antibiotico import Antibiotico
from modelo.errores import ValidationError

def test_antibiotico_valido():
    a = Antibiotico("Antibio A", 450, "Bovinos", 25000.0)
    assert a.dosis_kg == 450
    assert a.tipo_animal == "Bovinos"

def test_antibiotico_dosis_fuera_rango():
    with pytest.raises(ValidationError):
        Antibiotico("Antibio B", 350, "Bovinos", 1000.0)

def test_antibiotico_tipo_invalido():
    with pytest.raises(ValidationError):
        Antibiotico("X", 500, "Aves", 1000.0)
