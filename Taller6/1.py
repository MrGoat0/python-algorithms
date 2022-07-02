a = list(map(int, input().split()))
num = set(a)
for i in a:
    condi= 1000 - i
    if condi in num and i!=condi:
        print('SI')
        break
else:
    print('NO')