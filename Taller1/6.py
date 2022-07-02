X1=int(input())
Y1=int(input())
X2=int(input())
Y2=int(input())
r=(((X2-X1)**2)+((Y2-Y1)**2))**0.5
R=format(r,'.5f')
print('La distancia entre ('+str(X1)+',',str(Y1)+') y ('+str(X2)+',',str(Y2)+') es '+R)
