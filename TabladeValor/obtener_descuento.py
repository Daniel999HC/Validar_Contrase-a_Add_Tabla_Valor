def obtener_descuento(edad, es_miembro):
    # Definir las reglas de la tabla de decisión
    if edad < 18:
        if es_miembro:
            return "20%"
        else:
            return "10%"
    elif 18 <= edad <= 65:
        if es_miembro:
            return "10%"
        else:
            return "No descuento"
    else:  # edad > 65
        if es_miembro:
            return "30%"
        else:
            return "20%"

# Ejemplo de uso
edad = int(input("Ingrese la edad de la persona: "))
es_miembro = input("¿Es miembro? (sí/no): ").strip().lower() == 'sí'

descuento = obtener_descuento(edad, es_miembro)
print(f"El descuento aplicable es: {descuento}")