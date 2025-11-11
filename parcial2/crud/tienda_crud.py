# crud/tienda_crud.py
from datetime import date
from typing import List
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.producto import Producto
from modelo.errores import ValidationError

class TiendaCRUD:
    """
    Gestiona clientes, facturas y consultas.
    """
    def __init__(self):
        # clave = cédula, valor = Cliente
        self._clientes = {}

    # ----- CLIENTES -----
    def registrar_cliente(self, nombre: str, cedula: str) -> Cliente:
        if cedula in self._clientes:
            return self._clientes[cedula]
        cliente = Cliente(nombre, cedula)
        self._clientes[cedula] = cliente
        return cliente

    def obtener_cliente(self, cedula: str) -> Cliente:
        cliente = self._clientes.get(cedula)
        if not cliente:
            raise ValidationError(f"No existe cliente con cédula {cedula}")
        return cliente

    # ----- FACTURAS -----
    def crear_factura(self, cedula: str, fecha: date, productos: List[Producto]) -> Factura:
        if not productos:
            raise ValidationError("La factura debe tener al menos un producto.")
        cliente = self.obtener_cliente(cedula)
        factura = Factura(fecha, productos)
        cliente.agregar_factura(factura)
        return factura

    # ----- CONSULTAS -----
    def facturas_de_cliente(self, cedula: str) -> List[Factura]:
        cliente = self.obtener_cliente(cedula)
        return cliente.obtener_facturas()

    def productos_de_cliente(self, cedula: str) -> List[Producto]:
        cliente = self.obtener_cliente(cedula)
        return cliente.obtener_productos_comprados()

# Función solicitada en el enunciado:
def buscar_por_cedula(tienda: TiendaCRUD, cedula: str):
    """
    Retorna un diccionario con info de cliente, facturas y productos vendidos,
    según los requerimientos del enunciado.
    """
    cliente = tienda.obtener_cliente(cedula)
    facturas = cliente.obtener_facturas()
    productos = cliente.obtener_productos_comprados()

    return {
        "cliente": {
            "nombre": cliente.nombre,
            "cedula": cliente.cedula,
        },
        "facturas": [
            {
                "fecha": f.fecha,
                "total": f.total(),
                "productos": [p.nombre for p in f.productos]
            }
            for f in facturas
        ],
        "productos_vendidos": [p.nombre for p in productos],
    }
