def separar_digitos(n):
    # Convierte el número a una string haciéndo que sea más fácil obtener sus dígitos
    n_str = str(n)
    
    # Inicializar y vaciar lista para poder almacenar los números
    digitos_n = []
    
    # Iterar con los elementos de la string y añadir los dígitos a la lista
    for char in n_str:
        if char.isdigit():  # Verificar si los caracteres son dígitos
            digitos_n.append(int(char))
    
    return digitos_n

# Introducir un número para obtener sus dígitos
try:
    x = int(input("Introduzca un número: "))
    
    # Llamar la función para separar dígitos
    digitos_sep = separar_digitos(x)
    
    if digitos_sep:
        print("Los dígitos del número son:", digitos_sep)
    else:
        print("No se encontraron dígitos en la entrada.")
except ValueError:
    print("Entrada inválida, introduzca un número válido.") 