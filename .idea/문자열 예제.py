food = "Python's favorite food is perl"
print(food)
say = '"Python is very easy." he says.'
print(say)
food = 'Python\'s favorite food is perl'
print(food)
say = "\"Python is very easy.\" he says."
print(say)
multiline = "Life is too short\nYou need python"
print(multiline)
multiline='''
Life is too short
You need Python
'''
print(multiline)
multiline="""
Life is too short
You need Python
"""
print(multiline)
head = "Python"
tail = "is fun!"
print(head + tail)
a = "Python"
print(a*2)
# multistring.py
print("=" * 50)
print("My Program")
print("=" * 50)
a = "Life is too short, You need Python"
print(a[3])
print(a[0])
print(a[12])
print(a[-1])
print(a[-0])
print(a[-2])
print(a[-5])
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[0:3])
print(a[0:5])
print(a[0:2])
print(a[5:7])
print(a[12:17])
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)
a = "Pithon"
print(a[1])
print(a)
b = "Pithon"
print(b[:1])
print(b[2:])
print(a[:1] + 'y' + a[2:])
print("I eat %d apples."%3)
print("I eat %s apples."% "five")
number = 3
print("I eat %d apples."% number)
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days"%(number, day))
print("I haver %s apples"% 3)
print("rate is %s"% 3.234)
print("Error is %d%%"% 98)
print("%10s"% "hi")
print("%-10sjane."% 'hi')
print("%0.4f"% 3.42134234)
print("%10.4f"% 3.42134234)
a = "hobby"
print(a.count('b'))
a = "Python is best choice"
print(a.find('b'))
print(a.find('k'))
a = "Life is too short"
print(a.index('t'))
a = ","
print(a.join('abcd'))
a = "hi"
print(a.upper())
a = "HI"
print(a.lower())
a = " hi "
print(a.lstrip())
a = " hi "
print(a.rstrip())
print(a.strip())
a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a.split())
a = "a:b:c:d"
print(a.split(':'))
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
number = 3
print("I eat {0} apples".format(number))
number = 10
day = "three"
print("I ate {0} apples. so I was sock for {1} days.".format (number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{{ and }}".format())