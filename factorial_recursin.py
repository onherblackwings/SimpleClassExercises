def factorial(num):
    fac=num
    if num==1:
        return fac
    else:
        return fac*factorial(num-1)

num=input("Input a number for factorial: ")
print factorial(num)
