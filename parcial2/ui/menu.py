# ui/menu.py
from datetime import date
from crud.tienda_crud import TiendaCRUD, buscar_por_cedula
from modelo.antibiotico import Antibiotico
from modelo.control_plagas import ControlPlagas
from modelo.fertilizante import Fertilizante

def ejecutar_menu():
    tienda = TiendaCRUD()

    while True:
        print("\n--- TIENDA AGRÍCOLA ---")
        print("1. Registrar cliente")
        print("2. Crear factura")
        print("3. Buscar por cédula")
        print("4. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            cedula = input("Cédula: ").strip()
            tienda.registrar_cliente(nombre, cedula)
            print("Cliente registrado.")

        elif opcion == "2":
            cedula = input("Cédula cliente: ").strip()
            # para simplificar el ejemplo, creamos productos fijos
            print("Creando productos de ejemplo...")
            a = Antibiotico("Antibio A", 500, "Bovinos", 20000.0)
            cp = ControlPlagas("ICA-777", "Insecticida Z", 15, 8000.0, periodo_carencia_dias=10)
            f = Fertilizante("ICA-9", "Fert B", 30, 15000.0, date(2025, 1, 1))
            factura = tienda.crear_factura(cedula, date.today(), [a, cp, f])
            print(f"Factura creada. Total: {factura.total()}")

        elif opcion == "3":
            cedula = input("Cédula a consultar: ").strip()
            try:
                info = buscar_por_cedula(tienda, cedula)
            except Exception as e:
                print("Error:", e)
            else:
                print(f"\nCliente: {info['cliente']['nombre']} ({info['cliente']['cedula']})")
                print("Facturas:")
                for f in info["facturas"]:
                    print(f"  - Fecha: {f['fecha']}  Total: {f['total']}")
                    print("    Productos:", ", ".join(f['productos']))
                print("Productos totales comprados:", ", ".join(info["productos_vendidos"]))

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
