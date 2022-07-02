def repetidas(x, y):
    cad=sorted(set(x.split()))
    cad2=sorted(set(y.split()))
    repe=[]
    for i in cad:
        for j in cad2:
            if j == i:
                repe.append(j)
    return print(*repe)
x=input()
y=input()
repetidas(x, y)
