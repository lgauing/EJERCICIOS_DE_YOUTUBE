#el siguiente programa debería imprimir el numero 2 si se le ingresan como vaalores x=
# 5, y=1

from Ejercicio2_2 import *

#programa principal
x = int(input("Primer numero x: "))
y = int (input("Segundo número y: "))
print(maximo(x-3, minimo(x+2, y-1)))