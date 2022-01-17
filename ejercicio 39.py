#Escribir una función que , dado un número DNI, retorne True si el
# número es válido y false si no lo es.
#Para un número de DNI seea válido debe tener entre 6 a 8 dígitos
def DNivalido(dni):
    cantidad=0
    while dni!=0: 
        cantidad +=1
        dni = dni // 10
    return cantidad == 7 or cantidad == 8 
        
print(DNivalido(548))
print(DNivalido(58789954))



