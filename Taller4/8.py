def lista(n):
    cad=[]
    while True:
        x=(n//36)
        cad.append(n%36)
        n=x
        if x<36:
            cad.append(x)
            break
    final=cad[::-1]
    return final

def cual(n):
    N='0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z'
    cad=N.split()
    return cad[n]

n=int(input())
cad=lista(n)
result=[]
for i in cad:
    result.append(cual(i))
final=[]
if result[0]=='0':
    final=result[1:]
else:
    final=result[:]
final2=''
for i in final:
    final2+=i
    
print(final2)