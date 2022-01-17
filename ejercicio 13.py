>>> 11-(4%2+10)
1
>>> "30"+2
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    "30"+2
TypeError: can only concatenate str (not "int") to str
>>> "30"+"2"
'302'
>>> "hola"[len("hola")]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    "hola"[len("hola")]
IndexError: string index out of range
>>> len(124)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    len(124)
TypeError: object of type 'int' has no len()
>>> "hola" [len("fin")]
'a'
>>> "hola"[11-(4%2+10)]
'o'
>>> int("4")
4
>>> int(4)
4
>>> int("z")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    int("z")
ValueError: invalid literal for int() with base 10: 'z'
>>> int("4.")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int("4.")
ValueError: invalid literal for int() with base 10: '4.'
>>> 4<"f"
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    4<"f"
TypeError: '<' not supported between instances of 'int' and 'str'
>>> "palabra"="rama"
SyntaxError: can't assign to literal
>>> "palabra"=="rama"
False
>>> 
