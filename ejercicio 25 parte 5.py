


############### Ejercicio 15 ###############
anio=int(input("Anio: "))
if anio%4 != 0:
    print("No es bisiesto.")
else:
    if anio%100 != 0 or anio%400 == 0:
        print("Es bisiesto")
else:
    print("No es bisiesto")
