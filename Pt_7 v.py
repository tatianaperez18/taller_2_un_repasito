import math

# Función para calcular el promedio de una lista de números
def calcular_promedio(lista):
    return sum(lista) / len(lista)

# Función para calcular la mediana de una lista de números
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        # Si hay un número par de elementos, se promedian los dos elementos del medio
        medio_izquierdo = lista_ordenada[n // 2 - 1]
        medio_derecho = lista_ordenada[n // 2]
        mediana = (medio_izquierdo + medio_derecho) / 2
    else:
        # Si hay un número impar de elementos, se toma el elemento del medio
        mediana = lista_ordenada[n // 2]
    return mediana

# Función para calcular el promedio multiplicativo
def calcular_promedio_multiplicativo(lista):
    multiplicacion = 1
    for numero in lista:
        multiplicacion *= numero
    return multiplicacion ** (1 / len(lista))

# Función para calcular la potencia del mayor número elevado al menor número
def calcular_potencia_mayor_al_menor(lista):
    lista_ordenada = sorted(lista)
    mayor = lista_ordenada[-1]
    menor = lista_ordenada[0]
    return mayor ** menor

# Función para calcular la raíz cúbica del menor número
def calcular_raiz_cubica_del_menor(lista):
    lista_ordenada = sorted(lista)
    menor = lista_ordenada[0]
    return math.pow(menor, 1/3)

# Solicitar al usuario ingresar 5 números reales
numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Calcular el promedio
promedio = calcular_promedio(numeros)
print(f"Promedio: {promedio}")

# Calcular la mediana
mediana = calcular_mediana(numeros)
print(f"Mediana: {mediana}")

# Calcular el promedio multiplicativo
promedio_multiplicativo = calcular_promedio_multiplicativo(numeros)
print(f"Promedio Multiplicativo: {promedio_multiplicativo}")

# Ordenar los números de forma ascendente
ascendente = sorted(numeros)
print(f"Números ordenados de forma ascendente: {ascendente}")

# Ordenar los números de forma descendente
descendente = sorted(numeros, reverse=True)
print(f"Números ordenados de forma descendente: {descendente}")

# Calcular la potencia del mayor número elevado al menor número
potencia = calcular_potencia_mayor_al_menor(numeros)
print(f"Potencia del mayor número elevado al menor número: {potencia}")

# Calcular la raíz cúbica del menor número
raiz_cubica = calcular_raiz_cubica_del_menor(numeros)
print(f"Raíz cúbica del menor número: {raiz_cubica}")
