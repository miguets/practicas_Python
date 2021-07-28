# etapas de la vida
age = int(input("Introduce la edad a evaluar: "))

stage = None

if age >= 0 and age < 10:
    stage = "Infancia"
    print(stage)
elif age >= 10 and age < 20:
    stage = "Adolescencia"
    print(stage)
elif age >= 20 and age <= 30:
    stage = "Adultez"
    print(stage)
else:
    stage = "Etapa no reconocida"
    print(stage)