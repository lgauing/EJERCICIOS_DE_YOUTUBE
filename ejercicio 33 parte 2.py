


############### Ejercicio 23 ###############
frase=input("Frase: ")
l=input("Letra para buscar su posicion: ")
i=0
while i!=len(frase):
    if l!=frase[i]:
        print("No se encontro la posicion", i)
        i+=l
        continue
    print("Se encontro en la posicion", i)
    break