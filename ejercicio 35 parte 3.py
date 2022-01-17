


############### Ejercicio 26 ###############
mayor=0
numero=int(input("Numero primo: "))
while primo(numero):
    print("Suma de los digitos:",sumaDigitos(numero))
    digito=int(input("Digito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veses")
    if numero>mayor:
        mayor=numero
    numero=int(input("Numero primo: "))
print("Factorial de",mayor,":",factorial(mayor))  
