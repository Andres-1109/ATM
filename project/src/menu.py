print ("====Bienvenido al menu del cajero====")
print ("Elija una opcion: ")
print ("1. Consultar saldo")
print ("2. Retirar dinero")
print ("3. Depositar dinero")
print ("4. Salir")
    
opciones = int(input("Ingrese la opcion que desea: "))

while True: 
    while True: 
        if opciones >4 or opciones <1:
            print("Opción no válida, por favor seleccione una opción entre 1 y 4.")
            opciones =int(input("Seleccione una opción: "))
        elif opciones == 1:
            consultar_saldo()
            
        elif opciones == 2:
            retirar_dinero()
            
        elif opciones == 3:
            depositar_dinero()
            
        elif opciones == 4:
            print("saliendo del programa")
            break
        
        else:
            break
