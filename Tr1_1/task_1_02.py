a = []
for i in range(3):
    a.append(int(input()))
b = max(a)
a.remove(b)
if sum(a)>b:
    print('YES')
else:
    print('NO')
