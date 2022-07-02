def vertical(m):
    condi=False
    for i in range(4):
        for j in range(2):
            if (m[i][j]=='x') and (m[i][j+1]=='x') and (m[i][j+2]=='.'):
                condi=True
            if (m[i][j]=='x') and (m[i][j+1]=='.') and (m[i][j+2]=='x'):
                condi=True
    return condi
def horizontal(m):
    condi=False
    for i in range(2):
        for j in range(4):
            if (m[i][j]=='x') and (m[i+1][j]=='x') and (m[i+2][j]=='.'):
                condi=True
            if (m[i][j]=='x') and (m[i+1][j]=='.') and (m[i+2][j]=='x'):
                condi=True
            if (m[i][j]=='.') and (m[i+1][j]=='x') and (m[i+2][j]=='x'):
                condi=True
    return condi
def diagonal_inver(m):
    condi=False
    for i in range(2):
        for j in range(3,1,-1):
            if (m[i][j]=='x') and (m[i+1][j-1]=='x') and (m[i+2][j-2]=='.'):
                condi=True
            if (m[i][j]=='x') and (m[i+1][j-1]=='.') and (m[i+2][j-2]=='x'):
                condi=True
            if (m[i][j]=='.') and (m[i+1][j-1]=='x') and (m[i+2][j-2]=='x'):
                condi=True
    return condi
def diagonal(m):
    condi=False
    for i in range(2):
        for j in range(2):
            if (m[i][j]=='x') and (m[i+1][j+1]=='x') and (m[i+2][j+2]=='.'):
                condi=True
            if (m[i][j]=='x') and (m[i+1][j+1]=='.') and (m[i+2][j+2]=='x'):
                condi=True
            if (m[i][j]=='.') and (m[i+1][j+1]=='x') and (m[i+2][j+2]=='x'):
                condi=True
    return condi
def verificar(m):
    if diagonal(m) or diagonal_inver(m) or horizontal(m) or vertical(m): return print('YES')
    else: return print('NO')
def split(word): 
    return [char for char in word]

n=int(input())
for i in range(n):
    cad=[]    
    for i in range(4):
        x=input()
        p=split(x)
        cad.append(p)
    #print(cad)
    verificar(cad)