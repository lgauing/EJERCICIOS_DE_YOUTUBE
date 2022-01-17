>>> x=150
>>> type(x)
<class 'int'>
>>> x=13.5
>>> type(x)
<class 'float'>
>>> x="hola"
>>> type(x)
<class 'str'>
>>> x=False
>>> type(x)
<class 'bool'>
>>> x="46"
>>> type(x)
<class 'str'>
>>> 1+x
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    1+x
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> int(x)
46
>>> x
'46'
>>> 2+4
6
>>> type(x)
<class 'str'>
>>> x
'46'
>>> x=int(x)
>>> type(x)
<class 'int'>
>>> 1+x
47
>>> x="5hola"
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: '5hola'
>>> a="15.25"
>>> type(a)
<class 'str'>
>>> float(a)
15.25
>>> 
