a=int(input())
b=int(input())
m = (b*6)
h = ((a*(60))*(0.5))+(b*0.5)
x=720-h
x1=360-h
y=360-m
p=x-y
p1=x1-y
l=360-p
l1=360-p1
if p<l and p<l1:
    print(format(p, '.1f'))
elif p>l and p>l1:
    print(format(l1, '.1f'))
else:
    print(format(l, '.1f'))