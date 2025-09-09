
edad = int(input("Ingresa tu edad: "))
if edad < 0:
    print("Edad no válida.")
elif edad <= 12:
    print("Eres un niño o niña.")
elif edad <= 17:
    print("Eres un adolescente.")
elif edad <= 59:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
