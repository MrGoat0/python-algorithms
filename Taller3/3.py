a=int(input())
b=int(input())
c=int(input())
d=int(input())
z=210
while True:
    if (z%2==a) and (z%3==b) and (z%5==c) and (z%7==d):
        break
    z-=1
print(z)