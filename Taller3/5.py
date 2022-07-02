menor=None 
mayor=None
suma=0
n=int(input())
val=0
#---------------------------#
while val<n:
    x=int(input())
    if x == 1:
        mayor = x
        menor = x
    elif mayor is None or x>mayor:
        mayor = x
    elif menor is None or x<menor:
        menor = x 
    val +=1
    suma +=x    
print(mayor)
print(menor)
print(format((suma//n), '.0f'))