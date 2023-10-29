def mas_vocales(cadena):
    # Función para contar el número de vocales en una cadena
    def contar_vocales(cadena):
        vocales = "AEIOUaeiou"
        contador = 0
        for letra in cadena:
            if letra in vocales:
                contador += 1
        return contador

    return contar_vocales(cadena) >= 2

# Solicitar al usuario que introduzca una lista de cadenas separadas por comas
entrada_usuario = input("Ingrese una lista de cadenas separadas por comas: ")
lista_cadenas = entrada_usuario.split(',')

# Variable para rastrear si se encontró una cadena con dos o más vocales
encontrada = False

# Iterar a través de la lista
for cadena in lista_cadenas:
    if mas_vocales(cadena):
        print(f"Se encontró una cadena con dos o más vocales: {cadena.strip()}")
        encontrada = True

# Si no se encontró ninguna cadena, imprime 'No existe'
if not encontrada:
    print("No existe")
