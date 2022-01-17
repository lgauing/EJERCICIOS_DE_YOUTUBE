


############### Ejercicio 21 ###############
digitosEnLaLinea=0
cantLineas=0
titulo=input("Titulo del libro: ")
while titulo!="*":
    if titulo == "/":
        cantLineas+=1
        print("Linea completa,Aparecen",digitosEnLaLinea,"digitos")
        digitosEnLaLinea=0
    else:
        for caracter in titulos:
            if caracter in "0123456789":
                digitosEnLaLinea+=1
    titulo=input("Titulo del libro: ")
print("Fin. Se leyeron",cantLineas,"lineas")   