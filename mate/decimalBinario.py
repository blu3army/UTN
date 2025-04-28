print("Seleccione opción:")
print("1. Decimal a binario")
print("2. Binario a decimal")
print("3. Salir")

option = int(input("Opción: "))

if option == 1:
    decimal = int(input("Ingrese un número decimal: "))
    
    if decimal < 0:
        print("El numero debe ser positivo")

    if decimal == 0:
        print("0")


    # Acumulador de caracteres binarios
    binario = ""

    # FORMULA para ir de decimal a binario
    # Vamos dividiendo el valor por 2, usamos modulo para eso. Así obtenemos el resto


    # Recorremos el número decimal
    while decimal > 0:
        # Obtenemos el resto de la división entre 2
        resto = decimal % 2
        # Agregamos el resto al inicio del número binario
        binario = str(resto) + binario
        # Reducimos el número decimal a la mitad y lo convertimos a entero
        decimal = int(decimal / 2)
            
    print(f"El número en binario es: {binario}")


elif option == 2:   
    binario = input("Ingrese un número binario: ")

    # Validacion
    if not all( c in "01" for c in binario):
        print("Número binario no válido")


    decimal = 0

    # Formula ejemplo: digito * 2^3 + digito * 2^2 + digito * 2^1 + digito * 2^0 

    # Recorremos el número binario
    for i in range(len(binario)):
        # Obtenemos el exponente: longitud del binario - 1 - i
        exponente = len(binario) - 1 - i
        # Obtenemos el dígito en la posición i del binario
        digito = int(binario[i])
        # Multiplicamos el dígito por 2 elevado al exponente
        numero = digito * 2 ** exponente
        # Agregamos al total
        decimal += numero

    print(f"El número en decimal es: {decimal}")    
    
else:
    print("Saliendo")
    exit()