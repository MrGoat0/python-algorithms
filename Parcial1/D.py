n=int(input())
cont=0
for a in range(n):
    a+=1
    for b in range(a):
        b+=1
        if (((a**2)+(b**2))**0.5)<=n:
            if (((a**2)+(b**2))**0.5)%1==0:
                cont+=1
print(cont)
