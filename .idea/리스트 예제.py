odd = [1, 3, 5, 7 ,9]

a = [ ]
b [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

a = [1, 2, 3]
a
a[0]
a[0] + a[2]
a[-1]

a = [1, 2, 3, ['a', 'b', 'c']]
a[0]
a[-1]
a[3]
a[-1][0]
a[-1][-1]
a[-1][2]

a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0]

a = [1, 2, 3, 4, 5]
a[0:2]

a = "12345"
a[0:2]

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
b
c

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]
a[3][:2]

a = [1, 2, 3]
b = [4, 5, 6]
a + b
a * 3
str(a[2]) + "hi"
a[2] = 4
a
a[1:2]
a[1:2] = ['a', 'b', 'c']
a

a[1] = ['a', 'b', 'c']
a
a[1:3] = []
a
de; a[1]
a

a = [1, 2, 3]
a.append(4)
a
a.append([5,6])
a

a = [1, 4, 3, 2]
a.sprt()
a

a = ['a', 'c', 'b']
a.sort()
a

a = ['a', 'c', 'b']
a.reverse()
a

a = [1,2,3]
a.index(3)
a.index(1)
a.insert(0, 4)
a.insert(3, 5)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a.remove(3)

a = [1,2,3]
a.pop()
a

a = [1,2,3]
a.pop(1)
a

a = [1,2,3,1]
a.count(1)

a = [1,2,3]
a.extend([4,5])
a
b = [6, 7]
a.extend(b)
a

a = [1, 2, 3, 'a', 'b', 'c']
a.remove('a')
a

a = [1, 2, 3, 'a', 'b', 'c']
a.pop(4)
a

a = [1, 2, 3, 'a', 'b', 'c']
del a[4]
a

