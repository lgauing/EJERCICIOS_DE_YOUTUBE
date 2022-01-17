def DNIvalido(dni):
    cantidad= 0
    while dni!=0:
        cantidad = cantidad + 1
        dni=dni//10
    return cantidad==7 or cantidad==8

def lenUltimaPlabra(cadena):
    longitud=len(cadena)
    if longitud==0:
        return 0
    cantidad=0
    for i in range(longitud):
        if cadena[i]!=" ":
            cantidad = cantidad + 1
        else:
            if cadena[i]==" " and i<(longitud-1) and cadena[i+1] !=" ":
                cantidad=0
    return cantidad

def primerosTresDigitos(numero):
    while numero>=1000:
       numero=numero/10
    return int(numero) 

def obtenerIdentificacion(nombre,dni):
    nombre=nombre.strip()
    i=nombre[0:nombre.find(" ")]
    i=i+str(lenUltimaPlabra(nombre))
    i=i+str(primerosTresDigitos(dni))
    return i

print(obtenerIdentificacion("Erlyn stuard Naranjo Burgos    ", 123456))
print(primerosTresDigitos(123547))