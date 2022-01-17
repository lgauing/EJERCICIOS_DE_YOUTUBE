>>> s="   hola, ¿cómo estás?"
>>> s[::-1]
'?sátse omóc¿ ,aloh   '
>>> s[len(s)]
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    s[len(s)]
IndexError: string index out of range
>>> s[len(s)-1]
'?'
>>> s.count("o")
2
>>> s.count("Hola")
0
>>> s[-4:]
'tás?'
>>> s.find("o")
4
>>> s.strip()
'hola, ¿cómo estás?'
>>> x=s.upper()
>>> x==s
False
>>> x
'   HOLA, ¿CÓMO ESTÁS?'
>>> s
'   hola, ¿cómo estás?'
>>> s[14:].upper()
' ESTÁS?'
>>> s
'   hola, ¿cómo estás?'
>>> len(s)%2 != 0
True
>>> len(s)
21
>>> s.replace(" ", "*")
'***hola,*¿cómo*estás?'
>>> s.replace("z", "Z")
'   hola, ¿cómo estás?'
>>> 
