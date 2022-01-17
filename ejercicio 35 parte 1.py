


############### Ejercicio 26 ###############
direccion=input("Tu email: ")
caracterBuscado="@"
emailValido=False
for c in direccion:
    if c==caracterBuscado:
        emailValido=True
        break
if emailValido:
    print("Direccion valida")
else:
    print("Direccion Invalida")
