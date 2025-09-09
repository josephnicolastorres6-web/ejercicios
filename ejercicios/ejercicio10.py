
contraseña = input("Ingresa una contraseña: ")
# Verificar si la contraseña cumple con los requisitos
# Requisitos:
# - Al menos 8 caracteres
# - Contiene al menos una letra
# - Contiene al menos un número
tiene_letra = False
tiene_numero = False
for caracter in contraseña:
    if caracter.isalpha():
        tiene_letra = True
    if caracter.isdigit():
        tiene_numero = True
if len(contraseña) >= 8 and tiene_letra and tiene_numero:
    print("Contraseña válida.")
else:
    print("Contraseña inválida.")
    print("Debe tener al menos 8 caracteres, una letra y un número.")
