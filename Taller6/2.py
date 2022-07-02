def palindromo(s):
    num,space,do,up,suma = 256,[],0,len(s)-1,0
    ceros=[]
    for i in range(num):
        ceros.append(0)
    for c in s:
        ceros[ord(c)] += 1 
    for i in range(num):
        if ceros[i]%2 != 0:
            suma += 1
    if (len(s)%2 != 0):
        if suma==1:
            for i in range(len(s)):
                space.append('')
            for i in range(num):
                if ceros[i]%2 != 0:
                    ceros[i] -= 1
                    space[len(s)//2] = chr(i)
                while(ceros[i] > 0):
                    space[do] = chr(i)
                    space[up] = chr(i)
                    do,up = do+1,up-1
                    ceros[i] -= 2
    else:
        condi=True
        i = 0
        while i < 256 and condi:
            condi = ceros[i]%2 == 0
            i += 1
        if condi:
            for b in range(len(s)):
                space.append('')
            for i in range(num):
                while(ceros[i] > 0):
                    space[do] = chr(i)
                    space[up] = chr(i)
                    do,up = do+1,up-1
                    ceros[i] -= 2
    return space
cad= input()
test = palindromo(cad)
if len(test)==0:
    print('-1')
else:
    final=''
    for i in test:
        final+=i
    print(final)