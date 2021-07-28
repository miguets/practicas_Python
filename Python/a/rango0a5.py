numero = int(input("Introduce un numero entero cualquiera: "))

mayor = 5
menor = 0

a = numero > menor
b = numero < mayor

if a and b:
    print(f"el numero {numero} si se encuentra el rango de 0 a 5")
else:
    print(f"el numero {numero} no se encuentra en el rango de 0 a 5")