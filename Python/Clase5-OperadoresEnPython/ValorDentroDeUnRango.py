#  Ejercicio: Valor dentro de un rango
valor = int(input("Digite un número; "))
valorMinimo = 0
ValorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= ValorMaximo)
if dentroRango :
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} NO esta dentro del rango")