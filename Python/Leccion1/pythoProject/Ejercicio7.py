def calcular_salarios():
    # Definir variables
    suma = 0.0
    i = 1
    # Bucle para 5 empleados
    while i <= 5:
        print(f"Salario del empleado {i}:")
        horas = float(input("Digite las horas trabajadas: "))
        tarifa = float(input("Digite la tarifa por hora: "))

        # Calcular el salario
        salario = horas * tarifa

        # Mostrar el salario del empleado
        print(f"El salario es: ${salario:.2f}")

        # Acumular el salario en la suma total
        suma += salario

        # Incrementar el contador
        i += 1
    # Mostrar la suma de todos los salarios
    print(f"La suma de todos los salarios es: ${suma:.2f}")
# Llamar a la función
calcular_salarios()