if x1<x3 and x3<x2:
    if y1>y3 and y3>y2:
        print((x2-x3)*(y2-y3))
elif x3<x1 and x4>x1:
    if y3>y2 and y4<y2:
        print((x2-x4)*(y1-y3))
elif x1<x3 and x2>x3:
    if y1>y4 and y2<y4:
        print((x3-x1)*(y1-y3))
elif x3<x1 and x4>x1:
    if y3>y1 and y4<y1:
        print((x3-x2)*(y3-y1))