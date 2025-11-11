from datetime import date
from modelo.antibiotico import Antibiotico
from modelo.control_plagas import ControlPlagas
from modelo.fertilizante import Fertilizante
from modelo.cliente import Cliente
from modelo.factura import Factura

#crea instancias de productos (herencia y composición)
a = Antibiotico("Antibio A", 500, "Bovinos", 20000.0)
cp = ControlPlagas("ICA-777", "Insecticida Z", 15, 8000.0, periodo_carencia_dias=10)
#nuevo fertilizante para evidenciar herencia desde ProductoControl y composición en Factura
f = Fertilizante("ICA-9", "Fert B", 30, 15000.0, fecha_ultima_aplicacion=date(2025, 1, 1))

#composición: factura contiene una lista de Productos
fact = Factura(date.today(), [a, f, cp])

#composición: cliente contiene un historial de Facturas
cliente = Cliente("María Pérez", "987654321")
cliente.agregar_factura(fact)

#punto de ruptura para capturar pantallazos con el debugger (pdb)
breakpoint()

print("Total factura:", fact.total())
print("Total gastado por cliente:", cliente.total_gastado())
