import math
def prime_chk(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return 0
	return 1
counter=2
count=0
while(count!=10001):
	if prime_chk(counter):
		count = count+1
	counter=counter+1
print counter-1
