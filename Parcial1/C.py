n=int(input())
cont=0
a=1
b=a+1
c=b+1
while c<=n:
    while b<c:
        while a<b:
            if (a*a)+(b*b)==(c*c):
                cont+=1
            a+=1                  
        b+=1
    c+=1
print(cont)