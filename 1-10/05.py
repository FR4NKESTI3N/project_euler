def gcd(x,y):
	if(y==0):
		return x
	else:
		return gcd(y,x%y)
def lcm(x,y):
	return x*y/gcd(x,y)
x=1
for i in range(20,0,-1):
	x=lcm(i,x)
print x