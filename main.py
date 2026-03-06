#Aqui capturamos los datos del cliente y la venta realizada

print("\nBienvenido al nuevo sistema para registrar ventas\n" )
print("Por favor ingresa los datos de la venta que solicitaremos \n")

nombre = input("Nombre y apellido: ")
print("\nTiene el cliente membresia VIP? ")
print("\n1. Si")
print("2. No")

vip = int(input("\nIngrese el número de su elección: "))
while vip < 1 or vip > 2:
    print("Opcion no valida")
    vip = int(input("\nIngrese el número de su elección: "))

precio=int(input("\nIngrese el precio unitario del producto: "))
cantidad=int(input("\nIngrese la cantidad de productos: "))
descuento = precio * cantidad * 0.10
subt = precio * cantidad


print("\n################################")

print("\nFactura del cliente\n")

print(f"Cliente: {nombre}")

print(f"\nSubtotal: ${subt} ")
if vip == 1:
    print(f"Descuento: ${descuento}")
else:
    print("Descuento: $0")

if vip == 1:
    print(f"Total: ${subt - descuento}")
else:
    print(f"Total: ${subt}")

print("\nGracias por su compra, vuelva pronto!\n")

print("\n################################\n")

#Fin del programa