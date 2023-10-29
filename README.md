# taller_2_un_repasito

<a href='https://postimg.cc/LnZBsNmk' target='_blank'><img src='https://i.postimg.cc/LnZBsNmk/Sustainable-Badge-Logo.png' border='0' alt='Sustainable-Badge-Logo'/></a>     GRUPO: DEPORTIVO_TAPITAS                            
NOMBRES: Heidy Tatiana Perez, David Andrei Joya Reinel

### bueno empezamos con este repo:b
1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).

* para este use str, para obtener mas facil sus digitos, cree una lista vacia y recorri la lista char para luego añadirla a la lista.
* luego, retorne la lista, llame la funcion y imprimi el resultado.
[![punto2.png](https://i.postimg.cc/GpCc6Z5N/punto2.png)](https://postimg.cc/87ZQ6nDB)
2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.

* para este punto, utilice una funcion, separa el numero en entero y luego lo reste para dar la parte decimal.
* luego use str, para volver en numero en cadena y que asi se recorriera cada digito en el cilo for, lo hice para entero y decimal.
* no me salio bien:( el decimal no me funciono.
[![punto2.png](https://i.postimg.cc/26bp9Gxy/punto2.png)](https://postimg.cc/Vr8HdjpP)

3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

* para este use dos funciones, una para invertir el numero y la otra para verificar si son espejos.
* primero cree una funcion para invertir un numero, luego, se invierte el siguiente numero y los compara.
* luego se retornan y si cumplen se imprimen los resultados verdaderos o falsos.
[![punto2.png](https://i.postimg.cc/8k2PhJbN/punto2.png)](https://postimg.cc/Cd4g0KtQ)
4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.

* fue el mas dificil para mi, me toco pedir ayuda pero lo logre y logre entenderlo.
* importe math y cree una funcion, estableci un valor para la aproximacion, luego cree un ciclo para que  recorriera la cantidad de terminos dados, luego ya solo hice la ecuacion dada por taylor y se fue sumando con la aproximacion.
* estableci la x y la cantidad de terminos junto con el valor real usando la funcion math.
* use un cilo para calcular el error y restarlo del valor real a la aproximacion estableciendo que esta sea menor del 10 %
* tranforme el error en procentaje y que tuviera solo dos decimales, luego imprimi valores.
[![punto2.png](https://i.postimg.cc/Jzv5cQtP/punto2.png)](https://postimg.cc/sMPW37Yh) 

5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.

* use una funcion para calcular el maximo comun divisor, luego, use una relacion para hallar el minimo comun multiplo
* se retorna la funcion y se llama para luego imprimir el valor.
[![punto2.png](https://i.postimg.cc/Wz6KFHnD/punto2.png)](https://postimg.cc/2LyTgTgm)
6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in.

* para este use una funcion en donde se recorre la lista y se verifica si hay mas de un elemento igual en la lista con count.
* luego, solo imprime si es falso o verdadero.
[![punto2.png](https://i.postimg.cc/HWFMNLTk/punto2.png)](https://postimg.cc/0rdrMP6T)

7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

* primero, cree una funcion para contar las vocales.
* luego, con el uso de banderas se rastrea si tiene vocales o no.
[![punto2.png](https://i.postimg.cc/D0B6Kk6c/punto2.png)](https://postimg.cc/2LLh4tPq)
8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. Ejemplo:

* aqui, solo cree una funcion con una lista vacia para recorrer la lista 1 y verificar si hay elementos que no estan y asi guardarlos en la lista vacia.
[![punto2.png](https://i.postimg.cc/Fz0H8NxY/punto2.png)](https://postimg.cc/FksvJt8v)
9. Resolver el punto 7 del taller 1 usando operaciones con vectores.

[![punto2.png](https://i.postimg.cc/7YQvgp47/punto2.png)](https://postimg.cc/SJ8t41JN)
10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). Pista: Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?
* lo logre, :), para este use una funcion cree una lista vacia, recorrio la lista y verifico si este es multiplo de tres con modulo, y solo los guardo en la lista vacia.
* yo sabia que era igual que los digitos pero sumandolos y eso hice los sume hasta el numero 9, con la misma funcion del punto 2.

[![punto2.png](https://i.postimg.cc/7h4kC7gL/punto2.png)](https://postimg.cc/CBctXRry)
[![punto2.png](https://i.postimg.cc/YSmKb8R9/punto2.png)](https://postimg.cc/06xBNYLR)
