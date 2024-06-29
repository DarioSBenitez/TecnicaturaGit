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
# por lo que van a tener direcciones diferentes de memoria ya que las memorias ram son volatiles, los 0 y 1 se almacenan por
# un lapso de tiempo corto solo cuando corrio el programa y despues el capacitor (la memoria tiene internamente transistores y capacitores)
# que almaceno la tensión que representa un 1 lógico ya cayo a cero volts y ahora es un cero lógico por lo que puede que esa
# direccion de memoria la computadora ya la use para otra cosa, de ahi el nombre RAM (Random acces memory) 
# Memoria de acceso aleatorio.... y al ejecutar nuevamente nuestro código, nuestra variable va a
# apuntar a otra direccion de memoria diferente.