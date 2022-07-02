def analizar(cad):
    condición = "fútbol"
    cont = 5
    x = 0
    y = 6
    m = 0
    for i in range(x, (len(cad)-5)):
        f = cad[x:y]
        if condición not in f:
            cont += 1
            y += 1       
        else:
            if m < cont:
                m = cont
            cont = 5
            x = y-5
            y = x+6
    if m < cont:
        m = cont
    return print(m)
cad = input().lower()
analizar(cad)

