#Escribir una función que , dado un string, retorne la longitud dee la última palabra.
#se considera que las palabras están separadas por espacios poe uno o más espacios. También 
#podría haber espacios al principio o al final del string pasado por parámetro 
 
def lenUltimaPalabra(cadena):
    longitud=len(cadena)
    if longitud==0:
        return 0
    cantidad=0
    for i in range(longitud):
        if cadena[i]!=" ":
            cantidad=cantidad+1
        else:
            if cadena[i]==" " and i<(longitud-1) and cadena[i+1] !=" ":
                cantidad=0
    return cantidad
print(lenUltimaPalabra("Camino todas las tardes por el parque"))
print(lenUltimaPalabra("  Tarea de estructura   "))
