#Determinar cuál es la salida en pantalla si se ingresan los valores x=6, y=7:
#¿Qué sucede si los nombres de los pparámetros dentro de la función se cambian y se utilizan 
#los nombres a,b en lugar de los nombres x,y  ?

from Ejercicio1_1 import*

#Programa principal
x = int(input("Coordenada de eje x: "))
y = int(input("Cordenada de eje y:  "))
for i in range(3):
    z=cordenadaZ(x,y)
    x=x+1
    y=y+1
print(x," . ",y)