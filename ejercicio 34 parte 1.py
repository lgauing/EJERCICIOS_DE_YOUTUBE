


############### Ejercicio 24 ###############
cantidad=0
n=int(input("Numero: "))
while n!=0:
    primo=True
    for i in range(2,n):
        if n%i==0:
            primo=False
            break
    if primo:
        cantidad+=1
    n=int(input("Numero: "))
print("Primos",cantidad) 