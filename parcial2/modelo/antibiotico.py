#modelo/antibiotico.py
from modelo.producto import Producto
from modelo.errores import ValidationError

class Antibiotico(Producto):
    """
    Antibiotico: nombre, dosis (entre 400Kg y 600Kg), tipo_animal (Bovinos, Caprinos, Porcinos), precio.
    """
    TIPOS_ANIMAL_PERMITIDOS = {"Bovinos", "Caprinos", "Porcinos"}

    def __init__(self, nombre: str, dosis_kg: float, tipo_animal: str, precio: float):
        super().__init__(nombre=nombre, precio=precio)
        if dosis_kg is None or not (isinstance(dosis_kg, (int, float))):
            raise ValidationError("dosis_kg es obligatoria y debe ser número.")
        dosis_kg = float(dosis_kg)
        if not (400 <= dosis_kg <= 600):
            raise ValidationError("dosis_kg debe estar entre 400 y 600 (Kg).")
        if not tipo_animal or not isinstance(tipo_animal, str) or tipo_animal not in self.TIPOS_ANIMAL_PERMITIDOS:
            raise ValidationError(f"tipo_animal debe pertenecer a {self.TIPOS_ANIMAL_PERMITIDOS}.")
        self.dosis_kg = dosis_kg
        self.tipo_animal = tipo_animal
