from Ejercicio10_10 import *

socios_activos={1:["Amanda nuñez","175842",True], 2:["Rick Grimes","176544",True], 3: ["Juanita Sanchez","125842",True]}

print("***Cargar socios")
socios_activos=cargarSocios(socios_activos)

print("El club tiene ",len(socios_activos)," socios ")

print("REgistrar pago de cuotas ")
numero=int(input("Numero de socio: "))
socios_activos[numero][12]=True

print("***Modificanco fecha de ingrresos...")
socios_activos=modificarFecha(socios_activos, "130032018", "151515151")

print("Eliminar socio: ")
nombre=input("nombres y apellido: ")
numero=numeroSocio(socios_activos, nombre)
del socios_activos[numero]

imprimirListado(socios_activos)