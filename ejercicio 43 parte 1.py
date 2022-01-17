from Ejercicio7_7 import*

primaria=set()
secundaria=set()
print("Alumnos de primaria")
primaria=cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=cargarNombres(secundaria)

print("NOMBRE DE TODOS LOS ALUMNOS: ")
for nombre in primaria|secundaria:
    print(nombre)
    
print("NOMBRES COMUNES : ")
for nombre in primaria&secundaria:
    print(nombre)     

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA ")
for nombre in primaria-secundaria:
    print(nombre)
    