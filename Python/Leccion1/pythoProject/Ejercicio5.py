def calcular_factorial():
    # Definir variables
    num = int(input("Digite un número: "))

    # Verificar si el número es mayor o igual a 0
    if num >= 0:
        i = 1
        factorial = 1

        # Calcular el factorial
        while i <= num:
            factorial *= i
            i += 1

        # Mostrar el resultado
        print(f"El factorial de {num} es: {factorial}")
    else:
        print("El número debe ser mayor o igual a 0")


# Llamar a la función
calcular_factorial()
