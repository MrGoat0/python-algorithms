import math
a=int(input())
b=int(input())
c=int(input())
#---------------------------#
z=max(a,b,c)
y=max(a,b,c)
while True:
    if (z%a==0) and (z%b==0) and (z%c==0):
        break
    z +=y
print(z)