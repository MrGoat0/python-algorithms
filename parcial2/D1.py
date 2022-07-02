def analizar(cad):
    indice=[]
    posibles=[]
    for i in range(len(cad)):
        if (cad[i]=='f' and cad[i+1]=='ú'and cad[i+2]=='t'and cad[i+3]=='b'and cad[i+4]=='o'and cad[i+5]=='l') or (cad[i]=='F' and cad[i+1]=='ú'and cad[i+2]=='t'and cad[i+3]=='b'and cad[i+4]=='o'and cad[i+5]=='l') or (cad[i]=='f' and cad[i+1]=='ú'and cad[i+2]=='t'and cad[i+3]=='b'and cad[i+4]=='o'and cad[i+5]=='L'):
            indice.append(i)
        if len(indice)==2:
            cad_lon=cad[(indice[0]+1):((indice[1])+5)]
            posibles.append(len(cad_lon))
            indice.pop(0)
    return max(posibles)
cad=str(input())
cad_analizar=[]
for i in cad:
    cad_analizar.append(i)
print(analizar(cad_analizar))