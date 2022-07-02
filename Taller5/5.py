n=int(input())
x=input()
cad=x.split()
posición=list(map(int, cad[1:]))
k=int(cad[0])
p=int(cad[1])
power=int(cad[2])
condi=0
def ceros(n):
    cad=list()
    a=0
    while a<n:
        cad.append([0]*n)
        a+=1
    return cad
def change(n):
    m=ceros(n)
    for i in range(n):
        for j in range(n):
            a = abs(i-k)
            b = abs(j-p)
            condi = max(a,b)
            m[i][j] = (power - condi)
    return m
def imprimir(m):
    for i in range(len(m)):
        print(*m[i])
imprimir(change(n))