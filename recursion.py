def pow(x,y):
	if y==1:
		return x
	else:
		return x*pow(x,y-1)

print pow(12,3)