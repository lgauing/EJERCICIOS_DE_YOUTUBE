#imprimir una estructura directamente sin iterar

lista=[1, 2, 3, 4]
for elemento in lista:
    print(elemento)
    
articulos={589:["jabón para lavar platos", "limpieza",True],
          788:["aceite", "cosmética",False],
          259:["Cera para pisos", "limpieza",True]}
for clave, valor in articulos.items():
    print("Código: ", clave)
    print("Descripción: ",valor[0])
    print("Rubro ", valor[1])
    if valor[2]:
        print("Hay stock")
    else:
        print("Agotado")