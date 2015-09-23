


def binary(x):
    y=[]
    while x!=0:
        y.append(x%2)
        x=x/2
    y.reverse()
    y=''.join(map(str,y))
    y=int(y)

    return y

def another_binary(x):
    v=1;
    y=[]
    while v<=x/2:
        v=2*v
    n=x
    while v>0:
        if n<v:
            y.append(0)
        else:
            y.append(1)
            n=n-v;
        v=v/2
    y=''.join(map(str,y))
    y=int(y)    
    return y


x=input("number: ")
print binary(x)
print another_binary(x)
