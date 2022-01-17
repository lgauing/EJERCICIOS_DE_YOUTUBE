#Modificar la cantidad  de elemntos de la estructuura que se está iterrando

b={"a": [1,2,3], "b":[],"c":[],"d":[],"e":[4]}
for clave in b.keys():
    if b[clave] ==[]:
        del b[clave]
