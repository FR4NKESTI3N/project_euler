x=0																	#find 2(ab)+2(bc)+2(cd).......2(na)
for a in range(1,101):
	for b in range(1,101):
		if (a!=b):
			x=x+(a*b)
print x