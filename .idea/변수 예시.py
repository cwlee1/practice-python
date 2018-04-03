a = 1
b = 'python'
c = [1,2,3]

type(3)
a = 3
b = 3
a is b

import sys
sys.getrefcount(3)

a = 3
sys.getrefcount(3)

b = 3
sys.getrefcount(3)

c = 3
sys.getrefcount(3)

a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a,b] = ['python', 'life']
a = b = 'python'
a = 3
b = 5
a, b = b, a
a
b

a = 3
b = 3
del(a)
del(b)

a =[1,2,3]
b = a
a[1] = 4
a
b

a = {1, 2, 3}
b = a[:]
a[1] = 4
a
b

from copy import copy
b = copy(a)

b is a
