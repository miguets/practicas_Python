# numero mayor que otro
number1 = int(input("introduce un numero entero: "))
number2 = int(input("introduce otro numero entero: "))

if number1 > number2:
    print(f"el numero mayor es {number1}")
elif number1 == number2:
    print("ambos numeros son iguales")
else:
    print(f"el numero mayor es {number2}")
