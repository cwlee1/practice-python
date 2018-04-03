a = 18

while a > 0:
    print(a)

    if a == 3:
        print("break")
        a -= 1
        continue
    a -= 1

print("end")