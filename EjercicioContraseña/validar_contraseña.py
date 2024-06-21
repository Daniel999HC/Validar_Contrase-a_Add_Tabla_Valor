import re

def validar_contraseña(contraseña):
    # Verificar longitud
    if len(contraseña) < 8:
        return "Contraseña muy corta. Debe tener entre 8 y 10 caracteres."
    if len(contraseña) > 10:
        return "Contraseña muy larga. Debe tener entre 8 y 10 caracteres."
    
    # Verificar al menos 2 letras
    if len(re.findall("[a-zA-Z]", contraseña)) < 2:
        return "La contraseña debe tener al menos 2 letras."

    # Verificar al menos una letra mayúscula
    if not re.search("[A-Z]", contraseña):
        return "La contraseña debe tener al menos una letra mayúscula."

    # Verificar al menos una letra minúscula
    if not re.search("[a-z]", contraseña):
        return "La contraseña debe tener al menos una letra minúscula."

    # Verificar al menos un número
    if not re.search("[0-9]", contraseña):
        return "La contraseña debe tener al menos un número."

    # Verificar al menos un carácter especial
    if not re.search("[^a-zA-Z0-9]", contraseña):
        return "La contraseña debe tener al menos un carácter especial."

    return "Contraseña válida."

contraseña = input("Ingresa una contraseña: ")
resultado = validar_contraseña(contraseña)
print(f"Resultado: {resultado}")

#casos:
#1. Supere 10 caracteres:Resultado-->Contraseña muy larga. debe tener entre 8 a 10 caracteres.
#2. Menor a 8 caracteres:Resultado-->Contraseña muy corta. Debe tener entre 8 y 10 caracteres.
#3. Entre 8 a 10 caracteres:Resultado-->Pasa a la siguiente validacion.
#4. Si no hay letras mayuscula:Resultado-->La contraseña debe tener al menos una letra mayúscula.
#5. Si no hay 2 letras:Resultado-->La contraseña debe tener al menos 2 letras.
#6. Si no hay caracter especial:Resultado-->La contraseña debe tener al menos un carácter especial.
#7. Si no hay ningun numero:Resultado-->La contraseña debe tener al menos un número.
#8. Si no hay letras minuscula:Resultado-->La contraseña debe tener al menos una letra minúscula.
#9. si cumple todas las condiciones:Resultado-->Contraseña Valida.
