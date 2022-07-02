def repetidas(texto):
    pal=texto.split()
    pal.sort()
    repe = []
    for i in pal:
        repe.append(pal.count(i))
    x = max(repe)
    y = ''
    for j in pal:
        if pal.count(j) == x:
            y = j
            break
    return print(y, x)
texto = str(input())
repetidas(texto)