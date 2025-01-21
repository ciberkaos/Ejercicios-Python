cadena = "Python es maravilloso"
contador = 0
vocales = "aeiouAEIOU"

for caracter in cadena:
    if caracter in vocales:
        contador += 1
print(f"La cadena tiene {contador} vocales")