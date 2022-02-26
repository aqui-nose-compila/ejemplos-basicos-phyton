# Programa para conocer los tipos de datos
# Usaremos la función type() para conocer el tipo de datos

# Crear varias variables, cada una de un tipo de dato básico
entero = 5
flotante = 5.2
complejo = 5+6j
cadena = "¡Qué pasa tú!"

# Guardar en variables los tipos de datos de cada variable
tipo_entero = type(entero)
tipo_flotante = type(flotante)
tipo_complejo = type(complejo)
tipo_cadena = type(cadena)


# Mostrar por pantalla el contenido de las variables y sus tipos
print("Variable: ", entero, " - Tipo: ", tipo_entero)
print("Variable: ", flotante, " - Tipo: ", tipo_flotante)
print("Variable: ", complejo, " - Tipo: ", tipo_complejo)
print("Variable: ", cadena, " - Tipo: ", tipo_cadena)
