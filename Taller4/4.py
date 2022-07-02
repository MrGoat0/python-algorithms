def doc_product(x, y):
    cad=x.split()
    cad2=y.split()
    if len(cad)==len(cad2):
        sum=0
        for i in range(len(cad)):
            sum+=int(cad[i])*int(cad2[i])
        print(sum)   
    else: print('Error')
x=input()
y=input()
doc_product(x, y)