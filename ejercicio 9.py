>>> "buen"+"dia"
'buendia'
>>> a="buen"
>>> b="dia"
>>> a+" "+b
'buen dia'
>>> c=a+" "+b
>>> c
'buen dia'
>>> len(c)
8
>>> c[0]
'b'
>>> c[8]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    c[8]
IndexError: string index out of range
>>> c[1+1]
'e'
>>> c[len(c)]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    c[len(c)]
IndexError: string index out of range
>>> c[len(c)-1]
'a'
>>> 
