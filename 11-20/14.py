def collatz_sum(n):
	cnt=1
	while n!=1:
		if n&1:
			n=3*n+1
			cnt=cnt+1
		else:
			n=n/2
			cnt=cnt+1
	return cnt
M=10
m=13
for i in range(1000,1000000):
	tmp = collatz_sum(i)
	if tmp>M:
		m=i
		M=tmp

print m,M
