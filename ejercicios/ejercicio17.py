# Crear una lista vacía para la lista de compras
lista_compras = []
print(" Lista de compras inteligente")
print("Escribe los productos uno por uno.")
print("Cuando termines, escribe 'fin'.\n")
# Pedir productos al usuario hasta que escriba 'fin'
while True:
    producto = input("Agregar producto: ").strip()
    if producto.lower() == "fin":
        break  # Sale del bucle si escribe "fin"
    if producto != "":
        lista_compras.append(producto)
        print(f"'{producto}' agregado a la lista.")
    else:
        print("No puedes agregar un producto vacío.")
print("\n🧾 Tu lista de compras:")
for item in lista_compras:
    print("- " + item)
if not lista_compras:
    print("Tu lista de compras está vacía.")
print("\n¡Feliz compra! 🛒")