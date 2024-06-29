# Ejercicio con el operador or y not

# operador or no puede asistir al juego
vacaciones = False
diaDescanso = False
if vacaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("No puede asistir al juego")


# Operador or puede asistir al juego
vacaciones = False
diaDescanso = True
if vacaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("No puede asistir al juego")


# Operador not

# Operador or cambiando la lógica en el if
vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("No puede asistir al juego")
