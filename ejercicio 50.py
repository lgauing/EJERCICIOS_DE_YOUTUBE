#Buscar en una estructura a un determinado lemento que solo puede estar en un aestructura anidada

def empleadoosExiste(empleados, nombre):
    for datos in empleados.values():
        if datos[0]==nombre:
            return True
    return False

empleados={ 100: ["Stuard Naranjo", "Gerencia"],
200: ["Guadalupe Ríos", "ventas"],   
300: ["Leonel Campos","RR.HH"],
400: ["Oreana Lopez","Administración"]}

nombre=input("Nombre de empleado:")
if not empleadoosExiste(empleados, nombre):
    print("El empleado no se encuentra en la nómina")