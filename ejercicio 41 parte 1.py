#Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Patra ingresaar nombre coompleto y número de DNI de cada socio
#indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
#Precondición: el formato del nombre de los socios será: nombre aplellido.Podría ingresarse más de un nombre en cuyo caso será : nombvre1 nombre2 apellido
#Si un socio tuviera más de un apellido el usuario solo podrá ingresar uno
#Se debe validar que el número de Cédula tenga 7 u 8 dígitos.En caso contrario, el programa debe dejar al usuario en unn bucle hasta que ingrese unDNI correcto
#Por cada socio se debe imprimir un identificador único, el cuál estará formado por: el primer nombre, la cantidad de las letras del apellido y los 3 prmieros dígitos de su DNI.

from Ejercicio5_5 import *

nombre = input("nombre del socio:  ")
while nombre!="":
    dni=int(input("DNI del socio"))
    while not(DNIvalido(dni)):
        print("Numero invalido")
        dni=int(input("DNI del socio"))
    identificador=obtenerIdentificacion(nombre,dni)
    print("El identificador del socio es: ", identificador)
    nombre=input("nombre del socio: ")