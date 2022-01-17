>>> X="programar en python"
>>> X[-1]
'n'
>>> X[len(X)-1]
'n'
>>> cadena="hola"
>>> cadena.find("2")
-1
>>> "a" in "dátiles"
False
>>> "me gusta programar".count(" ")
2
>>> "me gusta programar".find(" ")
2
>>> cadena[0]="H"
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    cadena[0]="H"
TypeError: 'str' object does not support item assignment
>>> nueva="C"+cadena[1:]
>>> nueva
'Cola'
>>> X
'programar en python'
>>> X="hoy es día miércoles"
>>> X.replace("í", "i")
'hoy es dia miércoles'
>>> X
'hoy es día miércoles'
>>> X.replace("í","i").replace("é", "e")
'hoy es dia miercoles'
>>> X
'hoy es día miércoles'
>>> X.count("a")+X.count("e")+X.count("i")+X.count("o")+X.count("u")
6
>>> 
