def crear_dict(lst):
    cad=dict()
    for i in lst:
        nombre1,nombre2,result=i.split()
        cad[nombre1]=0
        cad[nombre2]=0
    return cad
def process(lst, dicc):
    for i in lst:
        nombre1,nombre2,result=i.split()
        if result == 'empate':
            dicc[nombre1]+=1
            dicc[nombre2]+=1
        elif result == nombre1:
            dicc[nombre1]+=2
        elif result == nombre2:
            dicc[nombre2]+=2
    return dicc
def orden(dicc):
    orden=[]
    for i in dicc:
        orden.append([dicc[i],i])
    orden.sort()
    orden.reverse()    
    return orden
num = int(input())
cont=0
lines = []
while cont < num:
    str = input()
    lines.append(str)    
    cont+=1
y=crear_dict(lines)
dicc=process(lines, y)
dicc_orden=orden(dicc)
for i in dicc_orden:
    print(i[1],i[0])