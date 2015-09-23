def factorial(num):
    ctr=num
    fac=1
    while ctr>0:
        fac=fac*ctr
        ctr-=1
    return fac    


fac=input("Input a number for factorial: ")
print factorial(fac)
