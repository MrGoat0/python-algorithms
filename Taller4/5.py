x=input()
cad=x.split()
num=[]

for i in cad:
    num.append(int(i))

condi=True
i=0

while i < (len(num)-1):
    pas = min(num[i],num[i+1])
    num[i] -= pas
    num[i+1] -= pas
    i += 1
i = 0    
while i < len(num) and condi:
    condi = num[i] == 0
    i += 1

if condi: print('SI')
else: print('NO')