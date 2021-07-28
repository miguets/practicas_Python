#   determinar por medio de un numero del 1-12 la estación del año
month = int(input("introduce el numero del mes en el que te encuentras (1-12): "))

season = None

if month == 12 or month == 1 or month == 2:
    season = 'Invierno'    # "winter"
elif month == 3 or month == 4 or month == 5:
    season = 'Primavera'    #  "spring"
elif month == 6 or month == 7 or month == 8:
    season = 'Verano'   #  "summer"
elif month == month == 9 or month == 10 or month == 11:
    season = 'Otoño'    #  "autumn"
else:
    season = 'mes equivocado'#  "wrong month"
print(season)
