# Pedir al usuario un número
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

# Mostrar la tabla del 1 al 10
print(f"\nTabla de multiplicar del {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
