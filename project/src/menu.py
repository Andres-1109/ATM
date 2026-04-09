from validations import validateInt
from services import consultar_saldo, retirar_dinero, depositar_dinero, ver_historial

def menu(balance, operationsHistory):
    """Despliega el menú principal del cajero y gestiona las opciones."""
    while True:
        print("==== Bienvenido al menú del cajero ====")
        print("Elija una opción:")
        print("  1. Consultar saldo")
        print("  2. Retirar dinero")
        print("  3. Depositar dinero")
        print("  4. Ver historial")
        print("  5. Salir")

        opcion = validateInt("Ingrese la opción que desea: ")

        if opcion < 1 or opcion > 5:
            print("Opción no válida, por favor seleccione entre 1 y 5.\n")
        elif opcion == 1:
            balance = consultar_saldo(balance, operationsHistory)
        elif opcion == 2:
            balance = retirar_dinero(balance, operationsHistory)
        elif opcion == 3:
            balance = depositar_dinero(balance, operationsHistory)
        elif opcion == 4:
            ver_historial(operationsHistory)
        elif opcion == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break