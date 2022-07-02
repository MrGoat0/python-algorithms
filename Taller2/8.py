a=int(input())
b=int(input())
c=int(input())
#--------------------------------------------------------#
x=b*c
y=a*c
z=a*b
#------------------------------------#
i=x%a
j=y%b
k=z%c
if i==0:
    print('El número '+str(a)+' es divisor de '+str(x))
    if j==0:
        print('El número '+str(b)+' es divisor de '+str(y))
        if k==0:
            print('El número '+str(c)+' es divisor de '+str(z))
    elif k==0:
        print('El número '+str(c)+' es divisor de '+str(z))        
elif j==0:
    print('El número '+str(b)+' es divisor de '+str(y))
    if k==0:
        print('El número '+str(c)+' es divisor de '+str(z))
elif k==0:
    print('El número '+str(c)+' es divisor de '+str(z))
else:
    print('Ninguna de las tres condiciones se cumple')