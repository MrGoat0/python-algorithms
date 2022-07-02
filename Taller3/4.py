a=int(input())
b=int(input())
c=int(input())
#-----------------------------#
val=0
while val<a:
    print('x'*b)
    print((' '*(b-1)+'x\n')*c, end='')
    print('x'*b)
    if val == (a-1):
        print('x\n'*(c-1),end='')
    elif val != a:
        print('x\n'*(c),end='')
    val +=1       
print('o')