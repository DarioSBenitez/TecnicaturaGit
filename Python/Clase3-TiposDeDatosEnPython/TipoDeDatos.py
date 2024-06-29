# Tipos de datos en Python
#Para mostrar el tipo de dato de una variable..

a = "Hola como estas"
print(type(a))

#Tambien si quiero indicarle a otro programador de que tipo debe ser la variable puedo escribir...

b: int = 1258 # aqui ademas de definir la variable entera b tambien le pongo una referencia de que es de tipo entera
print(type(b))

c = True
d = False
print(type(c))
print(type(d))

# Concatenación

palabra1 = "Los"
palabra2 = "tres"+" chiflados"
palabra3 = "eran ""cómicos"

print("En la película"+" "+palabra1+" "+palabra2+" "+palabra3)

num1 = "7"
num2 = "8"

suma = num1 + num2
print(suma) #se concatenan los strings

print(int(num1)+int(num2)) #Los strings se convierten a enteros y se suman

booleano = 5>7

if booleano:
    print("Es mayor")
else:
    print("es menor")
    
    # Entrada de usuario:
    
    entrada1 = int(input("ingresa un numero: "))
    print(entrada1)
    
    entrada2 = input("Esta entrada es un string: ")
    print(entrada2)
    
    entrada3 = float(input("Ingresa un numero con coma decimal: "))
    print(entrada3)
    
    entrada4 = bool(input("ingresa True o False"))
    print(entrada4)


# FUNCION INPUT (ENTRADA DEL USUARIO, Como entra los datos el usuario)

resultado = input("Digite un número") # Regresa un dato tipo string
print(resultado)

# Conversion de la entrada de datos

numero1 = input("Escribe el primer número")
numero2 = input("Escribe el segundo número")
resultado2 = numero1 + numero2
print(resultado2)


# el input guarda el dato como cadena. Si quiero especificar debo hacer (tipo(input))
numero1 = int(input("Ingresa un número desde el 10 en adelante"))
numero2 = int(input("Ingresa un número desde el 30 en adelante"))
resta5 = numero2 - numero1
print(resta5)