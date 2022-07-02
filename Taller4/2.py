def letra(x):
    cad='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    return cad[x]
    
cad1=str(input())
cad2=str(input())
cad='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
final=''

for i in range(len(cad1)):
    x=cad.index(cad1[i])
    y=cad.index(cad2[i])
    p=letra((x+y)%26)
    final+=p
print(final)