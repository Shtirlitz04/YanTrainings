a = int(input())
b = int(input())
c = int(input())
if c<0:
    print('NO SOLUTION')
elif a == 0:
    if b == c**2:
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')
else:
    if (c**2 - b) % a == 0:
        x = int((c**2 - b) / a)
        print(x)
    else:
        print('NO SOLUTION')
