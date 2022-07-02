def unir(cad):
    sub=''
    for i in cad:
        sub+=i
    return sub
def contar(cad, sub):
    sub_ca=''
    for i in sub:
        sub_ca+=i
    return cad.count(sub_ca)
def sub_cad(cad, cad_sepa, k):
    sub=dict()
    for i in range(0,len(cad_sepa)-k):
        sub[unir((cad_sepa[i:i+k]))]=(contar(cad, cad_sepa[i:i+k]))
    return sub 
    
    
cad=str(input())
k=int(input())
cad_sepa=[]
for i in cad:
    cad_sepa.append(i)
cad_repes=((sub_cad(cad, cad_sepa, k)))

ord = []
for p in cad_repes:
    ord.append((cad_repes[p],p))
ord.sort(reverse=True)
for i in ord:
    print(i[1])
    break