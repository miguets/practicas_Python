vacaciones = input("¿Tienes vacaciones?")
descanso = input("¿Tienes días de descanso?")

if vacaciones == "si" or vacaciones == "Si" or vacaciones == "SI" or vacaciones "sI":
    vacaciones == True
else:
    vacaciones = False

if descanso == "si" or descanso == "Si" or descanso == "SI" or descanso "sI":
    descanso = True
else:
    descanso = False

if vacaciones or descanso:
    print("puedes asistir al juego")
else:
    print("no puedes asistir al juego")