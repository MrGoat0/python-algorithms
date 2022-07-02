x=int(input())
y=int(input())
cont = 0
if y != 1:
    while x!=1:
        if x%y==0:
            cont +=1
            x= x//y
        elif x%y!=0:
            break
    print(cont)
else:
    print('inf')