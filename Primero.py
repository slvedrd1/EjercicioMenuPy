DEUDA = 100000

while True:

    print("--Menu--")
    print("1. Pago de tarjeta.")
    print("2. Simulacion de compras.")
    print("3. Salir.")

    while True:
        try:
            Opcion = int(input("Ingrese una opcion: "))
            break 
        except ValueError:
            print("Debe ingresar un numero del 1 al 3")  

    if Opcion == 1:

        print("Pago de tarjeta")
        MontoPagoCredito = int(input("Ingrese un monto para pagar la tarjeta de credito: $"))

        if MontoPagoCredito >= 0 and MontoPagoCredito <= DEUDA:
            DEUDA -= MontoPagoCredito
            print("Deuda: $",DEUDA)
        else:
            print("El monto a pagar excede la deuda.")


    elif Opcion == 2:

        print("Simulacion de compra")
        
        
        cantidad = int(input("Cuantas prendas desea comprar?: "))

        for i in range(cantidad):

            MontoCompra = int(input(f"\nIngrese el monto de la compra {i + 1}: $"))

            if MontoCompra >= 0:
                DEUDA += MontoCompra

                print("Deuda: $",DEUDA)
            else:
                print("Error monto no valido, el numero no debe ser negativo")


    elif Opcion == 3:
        print("Saliendo..")
        break

    else:
        print("Opcion no valida, intente otra vez.")
        








    


