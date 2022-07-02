a=int(input()) #1:00am
b=int(input()) #1:30am
c=int(input()) #2:00am
d=int(input()) #2:50am
if (a>=400 and a<600):
    print('Error 1:00am')      
    if (b>=400 and b<600):
        print('Error 1:30am')       
        if (c>=400 and c<600):
            print('Error 2:00am')            
            if (d>=400 and d<600):
                print('Error 2:30am')               
elif b>=400 and b<600:
    print('Error 1:30am')    
    if (c>=400 and c<600):
        print('Error 2:00am')       
        if (d>=400 and d<600):
            print('Error 2:30am')            
elif c>=400 and c<600:
    print('Error 2:00am')    
    if (d>=400 and d<600):
        print('Error 2:30am')        
elif d>=400 and d<600:
    print('Error 2:30am')
else:
    print('OK')
                