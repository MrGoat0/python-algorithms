def split(word): 
    return [char for char in word]
def verificar(m):
    condi=True
    mid=len(m)//2
    j=len(m)-1
    for i in range(0,mid):
        if m[i]!=m[j]:
            condi=False
        j-=1
    j=len(m)-1
    for i in range(0,mid):
        for k in range(len(m)):
            if m[k][i]!=m[k][j]:
                condi=False
        j-=1      
    if condi==True:
        return print('YES')
    else:
        return print('NO')  

n=int(input())
for i in range(n):
    cad=[]
    m=0
    y=input()
    for j in range(int(y)):
        x=input()
        p=split(x)
        cad.append(p)
    #print(cad)
    verificar(cad)