def agregarPasajeros(pasajeros):
    '''Agrega pasajeros a la lista y retorna'''
    nombre=input("Nombre -x para cortar: ") 
    while nombre!="x":
        dni=int(input("DNI: "))
        destino=input("Ciudad destino: ")
        pasajeros.append((nombre, dni, destino))
        nombre=input("Nombre -x para cortar ")
    return pasajeros


def agregarCiudades(ciudades):
    '''Agrega ciudades a la lista y la retorna '''
    ciudad=input("Ciudad -x para cortar: ")
    while ciudad!="x":
        pais=input("Pais: ")
        ciudades.append((ciudad, pais))
        ciudad=input("Ciudad -x para cortar: ")
    return ciudades


def buscarCiudad(pasajeros, dni):
    '''Dado el dni de un pasajero, lo busca en la lista y 
    retorna a la ciudad a la que viaja'''
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""

def cantidadPasajerosCiudad(pasajeros, ciudad):
    '''Dada una lista de pasajeros y ubna ciudad, retorna la 
    cantidad de pasajeros qiue viajan a esa ciudad.'''
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad    
def buscarPaisDestino(pasajeros, ciudades, dni):
    '''Dada un alista de pasajeros, una de ciudades y una dni
    retorna el pais al que viaja el pasajero con ese dni'''
    ciudadBuscada=buscarCiudad(pasajeros, dni)
    for ciudad in ciudades:
        if ciudad[0]==ciudadBuscada:
            return ciudad[1]
        return ""
    
def cantidadPasajerosPais(pasajeros, ciudades, pais):
    '''Dada una lista de pasajeros , una de viajes y un pais
    retorna la cantidad de pasajeros que viajan a ese pais '''    
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+1
    return cantidad