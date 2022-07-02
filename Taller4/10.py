def process_input(lst):
    result=[]
    producto={}
    for i in lst:
        nombre,n = i.split()
        n = int(n)
        if producto.get(nombre) != None: producto[nombre] += n
        else: producto[nombre] = n
    orden = list(producto.keys())
    orden.sort()
    
    for j in orden:
        result.append([j,producto[j]])
        
    return result

str = input()
lines = []
while str != 'FIN':
    lines.append(str)
    str = input()
print(process_input(lines))