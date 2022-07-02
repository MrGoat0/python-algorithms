op=str(input())
#------------------------------------#
if op == '+':
    a=int(input())
    b=int(input())
    print(a+b)
elif op == '-':
    a=int(input())
    b=int(input())
    print(a-b)
elif op == '*':
    a=int(input())
    b=int(input())
    print(a*b)
elif op == '/':
    a=int(input())
    b=int(input())
    print(a//b)
elif op == 'sqrt':
    a=int(input())
    print(int(a**0.5))
elif op == 'pow':
    a=int(input())
    b=int(input())
    print(a**b)