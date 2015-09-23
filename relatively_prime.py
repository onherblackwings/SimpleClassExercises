def relativelyprime(x,y):
    number=[x,y]
    xcounter=1
    ycounter=1
    topcounter=0
    x=[]
    y=[]
    z=[]

    while topcounter<=1:
        while xcounter<=number[topcounter]:
            while ycounter<=number[topcounter]:
                if xcounter*ycounter==number[topcounter]:
                    if topcounter==0:
                        x.append(ycounter)
                    else:
                        y.append(ycounter)

                ycounter+=1
            ycounter=1
            xcounter+=1
        ycounter=1
        xcounter=1
        topcounter+=1
        
    for i in x:
        for j in y:
            if i==j:
                z.append(j)

    if len(z)==1 and z[0]==1:
        return 1
    else:
        return 0

print relativelyprime(24,15)
print relativelyprime(16,45)
     







