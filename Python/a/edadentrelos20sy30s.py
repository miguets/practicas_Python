# edad entre los 20´s o 30´s

age = int(input("introduce tu edad:"))

decades20 = age >= 20 and age < 30
decades30 = age >= 30 and age < 40


if decades20 or decades30:
    print("estas entre el rango de los 20´s y 30´s")
    if decades20:
        print(f"estas en los 20´s con tu edad de {age}")
    else:
        print(f"estas en los 30´s con tu edad de {age}")
else:
    print("no estas dentro del rango")