a=int(input())
b=int(input())
for i in range(0, b):
    print('x'*a)
    if b>1:
        for j in range(0, b-2):
            if a>1:
                print('x'+'o'*(a-2)+'x')
            else:
                print('x'*a)                
        print('x'*a)
    break 