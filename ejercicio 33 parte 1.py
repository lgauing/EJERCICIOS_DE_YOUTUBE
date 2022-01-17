


############### Ejercicio 23 ###############
  while True:
    print("Opcion 1 - comenzar programa")
    print("Opcion 2 - imprimir listado")
    print("Opcion 3 - finalizar programa")
    opcion=int(input("Opcion elegida: "))
    if opcion==1:
        print("!Comenzamos!")
    elif opcion==2:
        print("Listado:")
        print("Nadia,Esteban,Mariela,Fernanda")
    elif opcion==3:
        print("Hasta la proxima")
        break
    else:
        print("Opcion incorrecta. Debe ingresar 1,2 o 3")