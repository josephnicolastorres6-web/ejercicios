import random
numero_secreto = random.randint(1, 10)
print(" Adivina el número del 1 al 10.")
print("Tienes 3 intentos.\n")
intento1 = int(input("Intento 1: "))
if intento1 == numero_secreto:
    print(" ¡Correcto! Adivinaste el número.")
else:
    intento2 = int(input("Intento 2: "))
    if intento2 == numero_secreto:
        print(" ¡Correcto! Adivinaste el número.")
    else:
        intento3 = int(input("Intento 3: "))
        if intento3 == numero_secreto:
            print(" ¡Correcto! Adivinaste el número.")
        else:
            print(" Has perdido. El número era:", numero_secreto)
