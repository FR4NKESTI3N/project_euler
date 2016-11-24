ar = [1,2,3]
i=2
s=2
while(ar[i]<4000000):
	i=i+1
	ar.append(ar[i-1]+ar[i-2])
	if (ar[i]%2==0):
		s=s+ar[i]
print s

