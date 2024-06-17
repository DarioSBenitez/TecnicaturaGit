respuesta = int(input("del 1 al 10, Como estuvo tu día? "))

if respuesta > 0 and respuesta <= 4:
    print("Lamento saber eso, arriba ese ánimo que la vida sigue!!")
elif respuesta > 4 and respuesta <= 7:
    print("Que bien!!, Hoy es un buen día para tener actitudes positivas :)")
elif respuesta > 7 and respuesta <= 10:
    print("Excelente!! solo resta disfrutar lo que amas hacer ya sea que estés trabajando o teniendo un día de descanso!!")
else:
    print("Tu respuesta no se condice con lo solicitado! :( ")   
    