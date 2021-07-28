# pedir nombre, id, precio, envio e imprimir toda la información

print("\t\tHola bienvenido")
name = input("introduce el nombre del libro adquirido: ")
identificator = int(input("introduce el numero de serie del libro: "))
price = float(input("introduce el precio del libro: "))
shipping = input("introduce si el envio es gratis (True / False): ")
if shipping == "True":
    shipping = True
elif shipping == "False":
    shipping = False
else: 
    print("El envio es incorrecto, tienes que escribir True o False")

if shipping == False:
    shippingprice = float(input("introduce el precio del envio: "))
else:
    shippingprice = 0

#ticket
print("\n\n\t\tTicket\n")
print("Libro:", name)
print("id:", identificator)
print("precio:", price)
if shippingprice == 0:
    print("Envio gratis")
else:
    print("Costo de envio:", shippingprice)

print("\nGracias por su compra\n    vuelva pronto\n\n")
