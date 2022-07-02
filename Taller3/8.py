a=int(input())
a=int(input())
b=int(input())
cad=''
cont=0
if a>1:
    for i in str(a):
        cad = i+cad
    for j in cad:
        if j != str(b):
            cont+=1
        if j == str(b):
            print(cont)
            break
    else:
        print('Imposible')
else:
    print(cont)