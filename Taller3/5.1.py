import math
a=[]
n=int(input())
val=0
while val<n:
    x=int(input())
    a.append(x)
    val+=1
suma=0
for i in a:
    suma+=i
print(max(a))
print(min(a))
print(suma//n)