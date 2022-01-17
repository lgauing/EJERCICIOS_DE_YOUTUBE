


############### Ejercicio 21 ###############
total=0
monto=float(input("Monto de una venta: $"))
while monto!=0:
    if monto<0:
        print("Monto no valido")
    else:
        total+=monto
    monto=float(input("Monto de una venta: $"))  
if total>1000:
    total=total-(total*0.1)
print("Monto total a pagar: $", total)   