


############### Ejercicio 20 ###############
suma=0
n=int(input("Numero positivo:"))
while n!=0:
    digito=n%10
    suma+=digito
    n=n//10
print("Suma de los digitos:", suma) 