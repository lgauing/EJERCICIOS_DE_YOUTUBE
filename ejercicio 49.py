#no considerar los extremos de un lista o los casos"Especiales"

lista= [1,3,4,4,6,7,7,8,0,9,9]

for i in range(len(lista)-1):
    if lista[i]==lista[i+1]:
        print(lista[i])