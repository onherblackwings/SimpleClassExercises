#function to return the product w/o using the "*" operator
def times(x,y):
    c=0
    p=0
    while c!=y:
        p=p+x
        c+=1
    return p
    
    
#variable declaration    
x=input("Please enter value to multiply w/o using operator: ")
y=input("Please enter another value to multiply w/o using operator: ")

#the output
print "The product of x=%d and y=%d is: %d" %(x,y,times(x,y))    



#ERROR CHECKING and VALIDATION
prod=x*y
print "Using the multiplication operator %d * %d is: %d " % (x,y,prod)
print "Are both values the same?", times(x,y)==prod

