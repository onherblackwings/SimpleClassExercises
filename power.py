x=2
y=8
z=1

checksum=x**y
print "%r raised to %r: " %(x,y)
while y!=0:
    #print "while y is: %r" %y
    #print "x is: %r" %x
    
    z=z*x
    #print "z*x is: %r " %z
   
    y-=1
    
print z
print "%r equals %r: " %(checksum, z)
print checksum==z


