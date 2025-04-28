def decimal_a_binario(decimal):
    if decimal < 0:
        return "El número debe ser positivo."
    

    binario = ""
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    
    return binario



# Al ingresar la opcion 2
# BINARIO A DECIMAL 
def binario_a_decimal(binario):
    # Validamos que el numero binario sea digito 1 o 0 unicamente, recorriendolo con un for 
    if not all(c in '01' for c in binario):
        return "Número binario inválido."
    
    # creamos el acumulador donde se sumara los digitos binarios
    decimal = 0

    # Luego creamos un rango con el tamaño de la cantidad de digitos binarios y los vamos recorriendo 
    # Cada digito de acuerdo a la posicion se elevará al cuadrado y luego los vamos sumando la variable decimal
    for i in range(len(binario)):
        exponente = len(binario) - 1 - i
        digito = int(binario[i])
        decimal += digito * 2 ** exponente
    #Retornamos la variable decimal
    return decimal






while True:
    print("\nSeleccione opción:")
    print("1. Decimal a binario")
    print("2. Binario a decimal")
    print("3. Salir")

    try:
        option = int(input("Opción: "))
        
        if option == 1:
            decimal = int(input("Ingrese un número decimal: "))
            resultado = decimal_a_binario(decimal)
            print(f"El número en binario es: {resultado}")
        
        elif option == 2:
            binario = input("Ingrese un número binario: ")
            resultado = binario_a_decimal(binario)
            print(f"El número en decimal es: {resultado}")
        
        elif option == 3:
            print("Saliendo...")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")

    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")