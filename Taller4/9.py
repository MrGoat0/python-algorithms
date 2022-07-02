x = input()
cad=x.split()
inv=list()
for i in cad:
    inv.append(int(i))
a=0
total=0
for i in range(len(inv)):
    for j in range(a,len(inv)):
        if len(inv) == (i+1) or len(inv) == (j+1):
            a += 1
        elif inv[i] > inv[j+1]:
            total += 1
        else:
            total += 0
print(total)