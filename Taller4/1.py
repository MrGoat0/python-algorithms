x = input()
cad=x.split()
cad2=[]
for i in cad:
    cad2.append(int(i))
y=''
cont=0
while cont < len(cad2):
    z = max(cad2)
    y = y + str(z) + ' '
    cad2 = cad2[cad2.index(z)+1:]
    z = max(cad2)
    cont = cad2.index(z)+1
print(y+str(max(cad2))+' ')