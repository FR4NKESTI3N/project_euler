import time
start=time.time()
def digit_sum(n):
	result=0
	while(n>0):
		result+=n%10
		n/=10
	return result
print digit_sum(2**1000),'----',time.time()-start,'----'