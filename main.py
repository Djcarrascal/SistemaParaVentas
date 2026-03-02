#Aqui capturamos los datos del cliente y la venta realizada

print("\nBienvenido al nuevo sistema para registrar ventas\n" )
print("Por favor ingresa los datos del cliente que te mencionaremos: \n")

input("Nombre y apellido: ")
input("\nDirección: ")
input("\nSi tiene membrecia escriba las siglas (ej: VIP), de lo contrario escriba (NO): ")
while True:
    try:
        precio=float(input("\nPrecio unitario del producto: "))
        cantidad=int(input("\nIngrese la cantidad de productos: "))
        break
    except ValueError:
        print("\n Dato ingresado inválido, solo se pueden ingresar números")

subt = precio * cantidad

print(f"\nEl valor total es: {subt:.3f} \n")