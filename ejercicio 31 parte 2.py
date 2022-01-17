


############### Ejercicio 21 ###############
totalPares=0
totalImpare=0
numero=int(input("Numero: "))
while numero!=0:
    pares=0
    impares=0
    while numero!=0:
        ultimoDigito=numero%10
        if ultimoDigito%2==0:
            pares+=1
            totalPares+=1
        else:
            impares+=1
            totalImpares+=1
        numero=numero//10
    print("El numero ingresado tiene",pares,"digitos pares y",impares,"digitos impares")    
    numero=int(input("Numero: "))   