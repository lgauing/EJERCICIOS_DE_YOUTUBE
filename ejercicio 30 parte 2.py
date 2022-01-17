


############### Ejercicio 20 ###############
positivos=0
n=int(input("Numero (0 para terminar): "))
while n!=0:
    if n>0:
        positivos+=1
    n=int(input("Numero (0 para terminar): "))
print("Cantidad de positivos:", positivos)