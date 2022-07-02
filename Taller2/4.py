x=int(input())
y=int(input())
if (x==0) and (y==0):
    print('El punto ('+str(x)+',',str(y)+') se encuentra en el origen')
elif (y==0):
    print('El punto ('+str(x)+',',str(y)+') se encuentra sobre el eje x')
elif (x==0):
    print('El punto ('+str(x)+',',str(y)+') se encuentra sobre el eje y')
elif (x>0) and (y>0):
    print('El punto ('+str(x)+',',str(y)+') se encuentra en el cuadrante I')
elif (x<0) and (y>0):
    print('El punto ('+str(x)+',',str(y)+') se encuentra en el cuadrante II')
elif (x<0) and (y<0):
    print('El punto ('+str(x)+',',str(y)+') se encuentra en el cuadrante III')
elif (x>0) and (y<0):
    print('El punto ('+str(x)+',',str(y)+') se encuentra en el cuadrante IV')