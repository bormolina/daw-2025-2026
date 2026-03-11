from cuenta_corriente import CuentaCorriente
from cuenta_ahorro import CuentaAhorro


if __name__ == "__main__":

    # Crear cuentas corrientes
    cc1 = CuentaCorriente("Ana López", "ES001", 500.0, 300.0)
    cc2 = CuentaCorriente("Carlos Ruiz", "ES002", 100.0, 200.0)

    # Crear cuentas ahorro
    ca1 = CuentaAhorro("Marta Gómez", "ES003", 1000.0, 2.5)
    ca2 = CuentaAhorro("Luis Torres", "ES004", 2500.0, 3.0)

    print("=== ESTADO INICIAL ===")
    print(cc1)
    print(cc2)
    print(ca1)
    print(ca2)

    print("\n=== INGRESOS (200€ para Ana y 500€ para Marta) ===")
    cc1.ingresar(200)
    ca1.ingresar(500)
    print(cc1)
    print(ca1)

    print("\n=== RETIRADAS (250€ para Carlos y 2000€ para Marta) ===")
    print("Retirada cc2 (250):", cc2.retirar(250))  # usa descubierto
    print("Retirada ca1 (2000):", ca1.retirar(2000))  # debería devolver false
    print(cc2)
    print(ca1)

    print("\n=== INTERESES ===")
    ca2.aplicar_intereses()
    print(ca2)

    print("\n=== COBRO COMISION ===")
    cc1.cobrar_comision()
    ca1.cobrar_comision()
    print(cc1)
    print(ca1)

    print("\n=== COMPROBAR IGUALDAD Y HASH ===")
    print("Para == creamos una cuenta corriente con mismo número que cc1 pero datos distintos")
    cc1_duplicada = CuentaCorriente("Roberto", "ES001", 0.0, 100.0)
    print("cc1 == cc1_duplicada:", cc1 == cc1_duplicada)

    print("Creamos un set con ambas cuentas (debería haber solo una)")
    cuentas_set = {cc1, cc1_duplicada}
    print("Número de cuentas en set:", len(cuentas_set))