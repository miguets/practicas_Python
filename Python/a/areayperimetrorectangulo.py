# Area y perimetro de un rectangulo

alto = int(input("Introduce la altura en cm de tu rectangulo: "))
ancho = int(input("introduce el ancho en cm de tu rectangulo: "))

perimetro = (alto + ancho) * 2
area = alto * ancho

print(f"el area de tu rectangulo es: {area} cm")
print(f"el perimetro de tu rectangulo es: {perimetro} cm")
