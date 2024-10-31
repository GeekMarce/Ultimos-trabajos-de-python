import random

estudiantes=["mario", "juan", "israel", "tom"]
ganador=random.choice(estudiantes)

print ('ingrese la palabra "ganador" para mostrar al ganador del sorteo')
palabra=input()

if palabra=="ganador":
    print("el ganador es",ganador)
else:
    print("Error: palabra incorrecta. No se puede mostrar al ganador.")