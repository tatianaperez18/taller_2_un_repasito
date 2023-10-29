def calcular_mcm(a, b):
    # Función para calcular el MCD
    def calcular_mcd(a, b):
        if b == 0:
            return a
        return calcular_mcd(b, a % b)

    # Acá se usa la relación al MCM = (a * b) / MCD
    mcd = calcular_mcd(a, b)
    mcm = (a * b) // mcd
    return mcm

# Entrada de dos números enteros desde el usuario
try:
    n1 = int(input("Ingrese el primer número entero: "))
    n2 = int(input("Ingrese el segundo número entero: "))
    
    mcm = calcular_mcm(n1, n2)
    print(f"El Mínimo Común Múltiplo de {n1} y {n2} es {mcm}")
except ValueError:
    print("Entrada inválida. Por favor, ingrese dos números enteros válidos.")
