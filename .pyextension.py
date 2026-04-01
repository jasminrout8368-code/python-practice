Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> myseries=pd.Series(['jasmin','sita','ita'],index=[10,20,30])
>>> print(myseries)
10    jasmin
20      sita
30       ita
dtype: object
>>> import pandas as pd
>>> myseries=pd.Series([2,4,5,6])
>>> print(myseries)
0    2
1    4
2    5
3    6
dtype: int64
>>> import pandas as pd
>>> dict={'A':1,'B':5,'C':9,'D':2}
>>> myseries=pd.Series(dict)
>>> print(myseries)
A    1
B    5
C    9
D    2
dtype: int64
>>> import pandas as pd
>>> dict={'A':2,'B':7,'C':0}
>>> myseries=pd.Series(dict)
>>> print(myseries['B'])
7
>>> import pandas as pd
>>> myseries=pd.Series([10,30,20,47,80,90,49,10,38])
>>> print(myseries[2:7])
2    20
3    47
4    80
5    90
6    49
dtype: int64
>>> import pandas as pd
myseries=pd.Series([10,20,30,40,50,60,70,80,90,100])
print(myseries.value)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(myseries.value)
  File "C:\Users\JASMIN ROUT\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\pandas\core\generic.py", line 6321, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'value'. Did you mean: 'values'?
