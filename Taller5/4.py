x = int(input())
y = 0
c = []
while x != y:
    M = []
    for i in range(4):
        M.append([0]*4)
    z = 0
    while z != 4:
        m = input()
        w = 0
        for k in m:
            M[z][w] = k
            w += 1
        z += 1
    a = False
    for i in range(4):
        if a == False:
            for j in range(4):
                if j + 2 <= 3:
                    if M[i][j] == 'x' and M[i][j+1] == 'x' and M[i][j+2] == '.':
                        a = True
                        break
                    elif M[i][j] == 'x' and M[i][j+1] == '.' and M[i][j+2] == 'x':
                        a = True
                        break
                    elif M[i][j] == '.' and M[i][j+1] == 'x' and M[i][j+2] == 'x':
                        a = True
                        break
                else:
                    pass
        else:
            break
                
    b = False
    for i in range(4):
        if b == False:
            for j in range(4):
                if i + 2 <= 3:
                    if M[i][j] == 'x' and M[i+1][j] == 'x' and M[i+2][j] == '.':
                        b = True
                        break
                    elif M[i][j] == 'x' and M[i+1][j] == '.' and M[i+2][j] == 'x':
                        b = True
                        break
                    elif M[i][j] == '.' and M[i+1][j] == 'x' and M[i+2][j] == 'x':
                        b = True
                        break
                else:
                    pass
        else:
            break
        
    c = False
    for i in range(4):
        if c == False:
            for j in range(4):
                if i + 2 <= 3 and j + 2 <= 3:
                    if M[i][j] == 'x' and M[i+1][j+1] == 'x' and M[i+2][j+2] == '.':
                        c = True
                        break
                    elif M[i][j] == 'x' and M[i+1][j+1] == '.' and M[i+2][j+2] == 'x':
                        c = True
                        break
                    elif M[i][j] == '.' and M[i+1][j+1] == 'x' and M[i+2][j+2] == 'x':
                        c = True
                        break
                else:
                    pass
        else:
            break

    d = False
    for i in range(4):
        if d == False:
            for j in range(4):
                if i + 2 <= 3 and j - 2 >= 0:
                    if M[i][j] == 'x' and M[i+1][j-1] == 'x' and M[i+2][j-2] == '.':
                        d = True
                        break
                    elif M[i][j] == 'x' and M[i+1][j-1] == '.' and M[i+2][j-2] == 'x':
                        d = True
                        break
                    elif M[i][j] == '.' and M[i+1][j-1] == 'x' and M[i+2][j-2] == 'x':
                        d = True
                        break
                else:
                    pass
        else:
            break

    if a == True or b == True or c == True or d == True:
        print('YES')
    else:
        print('NO')
        
    y += 1