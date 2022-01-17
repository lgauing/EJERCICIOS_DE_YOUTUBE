>>> cadena="programación en python"
>>> cadena[6]
'm'
>>> len(cadena)
22
>>> cadena[21]
'n'
>>> i=len(cadena)-1
>>> cadena[i]
'n'
>>> i
21
>>> cadena[len(cadena)-1]
'n'
>>> cadena[0:10]
'programaci'
>>> cadena[10:]
'ón en python'
>>> cadena[:10]
'programaci'
>>> cadena[:13]
'programación '
>>> cadena[:13:2]
'pormcó '
>>> cadena[::2]
'pormcó npto'
>>> cadena[::-1]
'nohtyp ne nóicamargorp'
>>> cadena[-1:]
'n'
>>> cadena.find("python")
16
>>> cadena.find("p")
0
>>> cadena.find("z")
-1
>>> cadena.find("z") == -1
True
>>> "python" in cadena
True
>>> precio="40"
>>> int(precio)
40
>>> type(int(precio))
<class 'int'>
>>> cadena.upper()
'PROGRAMACIÓN EN PYTHON'
>>> cadena.lower()
'programación en python'
>>> cadena
'programación en python'
>>> "6709".upper()
'6709'
>>> cadena.title()
'Programación En Python'
>>> cadena.capitalize()
'Programación en python'
>>> a="      hola"
>>> a.strip()
'hola'
>>> a="     hola    chau     "
>>> a.strip()
'hola    chau'
>>> cadena
'programación en python'
>>> cadena.count("p")
2
>>> cadena.count("o")
2
>>> cadena.replace("python", "***")
'programación en ***'
>>> cadena
'programación en python'
>>> cadena.replace("a", "-")
'progr-m-ción en python'
>>> cadena.replace("z", "i")
'programación en python'
>>> cadena.replace("ó", "o")
'programacion en python'
>>> 
