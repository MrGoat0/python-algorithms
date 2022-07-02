x=int(input())
if x>1:
    for i in range(2,x+1):
        while (x%i)==0:
            print(str(x)+'\t|'+'\t'+str(i))
            x = x//i
        if x==1:
            break
print('1')


#print(str(x)+'\t|'+'\t'+str(y))
