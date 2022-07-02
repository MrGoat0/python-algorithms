def quitar(d):
    p=list(d.values())
    x=max(p)
    while True:
        for i in p:
            if i==x:
                p.pop(p.index(i))
                break
        else: break
        #break     
    return p
n=input().split()
d={}
for i in n:
    i=int(i)
    d[i]=d.get(i,0)+1
moda=max(d.values())
cont=0
for i in d:
    if d.get(i)==moda:
        cont+=1
if cont==len(d):
    print('no existe')
else:
    dic=quitar(d)
    moda2=max(dic)
    posi=dic.index(moda2)
    cont=0
    for i in d:
        if d.get(i)==moda2:
            cont+=1
    if cont==1:
        for i in d:
            if d.get(i)==moda2:
                print(i)
                break
    else: 
        print('multiples soluciones')