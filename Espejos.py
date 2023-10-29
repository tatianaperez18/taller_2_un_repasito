def numero_espejo(n1, n2):
    # Función para invertir un número
    def invertir_n(numero):
        n_str = str(numero)
        n_invertido = int(n_str[::-1])
        return n_invertido

    # Invierte el segundo número y compara
    n2_invertido = invertir_n(n2)
    
    if n1 == n2_invertido and n2 == invertir_n(n1):
        return True
    else:
        return False

# Entrada de dos números enteros desde el usuario
try:
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    
    if numero_espejo(n1, n2):
        print("Los números", n1, "y", n2, "son espejos.")
    else:
        print("Los números" , n1, "y", n2, "no son espejos.")
except ValueError:
    print("Entrada inválida. Por favor, ingrese dos números enteros válidos.")
