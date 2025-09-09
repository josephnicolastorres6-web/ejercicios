
cantidad = int(input("¿Cuántos números vas a restar?:$ "))
resultado = float(input("Ingresa el primer número:$ "))
for i in range(2, cantidad + 1):
    numero = float(input(f"Ingresa el número {i}: "))
    resultado -= numero
print("El resultado de la resta acumulativa es:", resultado)
