N=input()
P=input()
cad=N.split()
cad2=P.split()
cont=0
nope=0
mal=list()
mal1=cad[1]
for k in cad2:
    if int(k) >= int(cad[1]):
        mal.append(k)
for i in cad2:
    if len(mal)==0:
        print(len(cad2))
        break
    else:
        for j in range(len(mal)):
            if int(i) >= int(mal[j]):
                nope+=1
                break
            if int(i)<=int(cad[1]):
                cont+=1
                break
        if nope>1:
            print(cont)
            break