a = int(input())
b = a*a
l = []
for i in range(b):
    l.append(i)
print(l)
l2 = [l[i:i+a] for i in range(0, len(l), a)]
print(l2)
for i in range(1, len(l2), 2):
    l2[i].reverse()
for i in range(a):
    print(*l2[i])