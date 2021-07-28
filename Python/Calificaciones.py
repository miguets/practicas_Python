qualification = float(input("introduce la calificación obtenida: "))
note = None
if 0 <= qualification < 6:
     note = 'F'
elif 6 <= qualification < 7:
    note = 'D'
elif 7 <= qualification < 8:
    note = 'C'
elif 8 <= qualification < 9:
    note = 'B'
elif 9 <= qualification <= 10:
    note = 'A'
else:
    note = "Valor incorrecto"
print(note)