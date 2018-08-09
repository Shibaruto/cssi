>>> d = {'A':['RS', 'LS', 'UC', 'LR'], 'B': ['TG', 'JM', 'CA', 'DS']}
>>> d['B']
['TG', 'JM', 'CA', 'DS']
>>> a = {}
>>> b = dict()
>>> a
{}
>>> b
{}
>>> d['C'] = ['CE', 'EP', 'TD', 'MM']
>>> d
{'A': ['RS', 'LS', 'UC', 'LR'], 'C': ['CE', 'EP', 'TD', 'MM'], 'B': ['TG', 'JM', 'CA', 'DS']}
>>> d['D'] = ['EB', 'CM', 'EA', 'RR']
>>> d['E'] = ['SH', 'RD', 'DK', 'CC']
>>> len(d)
5
>>> for i in d:
...     print i
...
A
C
B
E
D
>>> for i in d:
...     print d[i]
...
['RS', 'LS', 'UC', 'LR']
['CE', 'EP', 'TD', 'MM']
['TG', 'JM', 'CA', 'DS']
['SH', 'RD', 'DK', 'CC']
['EB', 'CM', 'EA', 'RR']
>>> for i in d:
...     print i, "=", d[i]
...
A = ['RS', 'LS', 'UC', 'LR']
C = ['CE', 'EP', 'TD', 'MM']
B = ['TG', 'JM', 'CA', 'DS']
E = ['SH', 'RD', 'DK', 'CC']
D = ['EB', 'CM', 'EA', 'RR']
>>> d.has_key("p")
False
>>> d.keys()
['A', 'C', 'B', 'E', 'D']
>>> d.values()
[['RS', 'LS', 'UC', 'LR'], ['CE', 'EP', 'TD', 'MM'], ['TG', 'JM', 'CA', 'DS'], ['SH', 'RD', 'DK', 'CC'], ['EB', 'CM', 'EA', 'RR']]
>>>
>>> for i in d.values():
...     print i
...
['RS', 'LS', 'UC', 'LR']
['CE', 'EP', 'TD', 'MM']
['TG', 'JM', 'CA', 'DS']
['SH', 'RD', 'DK', 'CC']
['EB', 'CM', 'EA', 'RR']

>>> for i,j in d.items():
...     print i, "=", j
...
A = ['RS', 'LS', 'UC', 'LR']
C = ['CE', 'EP', 'TD', 'MM']
B = ['TG', 'JM', 'CA', 'DS']
E = ['SH', 'RD', 'DK', 'CC']
D = ['EB', 'CM', 'EA', 'RR']

>>> if d.has_key("F"):
...     d.pop("F")
...
>>> d
{'A': ['RS', 'LS', 'UC', 'LR'], 'C': ['CE', 'EP', 'TD', 'MM'], 'B': ['TG', 'JM', 'CA', 'DS'], 'E': ['SH', 'RD', 'DK', 'CC'], 'D': ['EB', 'CM', 'EA', 'RR']}
>>> if d.has_key("C"):
...     d.pop("C")
...
['CE', 'EP', 'TD', 'MM']
>>> d
{'A': ['RS', 'LS', 'UC', 'LR'], 'B': ['TG', 'JM', 'CA', 'DS'], 'E': ['SH', 'RD', 'DK', 'CC'], 'D': ['EB', 'CM', 'EA', 'RR']}
