# Determinar si es mayor de edad
adult = 18
age = int(input("introduce la edad de la persona a evaluar: "))

if age >= adult:
    print(f"La persona con la edad {age} es mayor de edad")
else:
    print(f"La persona con la edad {age} es menor de edad")