x=int(input())
y=int(input())
w=int(input())
h=int(input())
#---------------------------------------#
a=w-x
b=h-y
if (x<y)and(x<a)and(x<b):
    print(x)
elif (y<x)and(y<a)and(y<b):
    print(y)
elif (a<x)and(a<y)and(a<b):
    print(a)
else:
    print(b)