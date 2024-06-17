# Las variables en Python son dinamicas, esto quiere decir que el valor puede cambiar segun le asigno un nuevo valor.

miVariable = 3 # miVariable toma el valor 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura" # ahora miVariable toma un string
print(miVariable)
miVariable = 3.5 # ahora miVariable toma un valor real, (Flotante!)
print(miVariable)

x = 10
y = 2
z = x + y

print(id(x))
print(id(y))
print(id(z))

# La variable x apunta a la direccion de memoria x648 donde esta guardado el valor 10
# con id mostramos la direccion de memoria a la que apunta la variable x

# Los literales se escriben x648, la variable y = x272, la variable z = x592. Estos valores cambian cada vez que se ejecuta el programa
# porque la memoria es volatil y cada vez que se vuelve a ejecutar el programa, las variables apuntan a direcciones diferentes de memoria
# por lo que van a tener direcciones diferentes.

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
    
    