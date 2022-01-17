#cargar  todos los datos en una misma lista cuando deberían ser diferentes

def cargarMercaderias(mercaderias):
    codigo=int(input("codigo: "))
    while codigo!=0:
        articulo=[]
        descripcion=input("DEscripcion: ")
        articulo.append(descripcion)
        rubro=input("Rubro: ")
        articulo.append(rubro)
        mercaderias[codigo]=articulo
        codigo=int(input("Código: "))
    return mercaderias

productos={}
productos=cargarMercaderias(productos)
for codigo, datos in productos.items():
    print(codigo, "-Descripcion",datos, "-Rubros")