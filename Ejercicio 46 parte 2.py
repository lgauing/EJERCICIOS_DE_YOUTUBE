from ast import While


def cargarSocios(socios):
    numero=int(input("Numero de socio: "))
    while numero !=0:
        nombre=input("Nombre y apellidos: ")
        fecha = input("Fecha de ingreso :")
        cuota =input("¿Cuota al día ? s/n :") 
        pago=cuota.lower()=="s"
        socios[numero]=[nombre,fecha,pago]
        numero =int(input("Numero del socio: "))
    return socios

def modificarFecha(socios, fecha_anterior, fecha_nueva):
    for datos in socios.values():
        if datos[1]==fecha_anterior:
              datos[1]=fecha_nueva
    return cargarSocios

def numeroSocio(socios,nombre):
    for numero,datos in socios.items():
        if datos[0].lower()==nombre.lower:
            return numero
    return 0

def formatoFecha(fecha):
    return fecha[:2]+"/"+fecha[2:4]

def imprimirListado(socios):
    for numero,datos in socios.items():
        print("-Numero: ", numero)
        print("-Nombre: ", datos[0])
        print("-Fecha de ingreso: ", formatoFecha(datos[1]))
        if datos[2]:
            print("-Cuota del día")
        else:
            print("-En deuda")
        print("---------")
    return None 
              