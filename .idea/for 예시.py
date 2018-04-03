test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

a = range(10)
a

a = range(1, 11)
a

sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end="")
    print('')

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)

