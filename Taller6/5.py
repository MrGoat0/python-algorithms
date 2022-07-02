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
if cont==1:
    print('unimodal')
elif cont==2:
    print('bimodal')
else:
    print('multimodal')