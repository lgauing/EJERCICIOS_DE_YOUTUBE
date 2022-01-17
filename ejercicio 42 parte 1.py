from Ejercicio6_6 import *

pasajeros =[ ]
ciudades =[ ]
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudadess")
    print("3. Buscar ciudad destino mediante DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar pais destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un pais")
    print("7. Salir del proograma")
    
    opcion=int(input("Accion de ejecutar: "))
    if opcion==1:
        print("AGREGAR PASAJEROS")
        pasajeros=agregarPasajeros(pasajeros)  
    elif opcion==2:
        print("AGREGAR CIUDADES")
        ciudades=agregarCiudades(ciudades)
    elif opcion==3:
        dni=int(input("DNI: "))
        print("el pasajero viaja a ", buscarCiudad(pasajeros, dni))
    elif opcion==4:
        ciudad=input("Ciudad : ")
        print("Viajan ",  cantidadPasajerosCiudad(pasajeros,ciudad),"pasajeros")
    elif opcion==5:
        dni=int(input("DNI: "))
        print("Viaja a ", buscarPaisDestino(pasajeros, ciudades, dni))   
    elif opcion==6:
        pais=input("Pais: ")
        print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais))
    elif opcion==7:
        break