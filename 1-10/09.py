import time
start_time = time.time()
for a in range(1,501):
	for b in range(1,501):
		#c=1000-a-b
		#if (a*a+b*b==c*c):
		if (a*b)==1000*(a+b-500):					#FASTER!!!. about 46%
			c=1000-a-b
			print a*b*c,a,b,c
			break
print("--- %s seconds ---" % (time.time() - start_time))