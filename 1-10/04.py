def is_palindrome(n):
	flag=1
	string = str(n)
	length = len(string)
	for i in range((length/2)):
		if string[i] != string[length-1-i]:
			flag=0
	return flag
largest = 9009
for i in range(101,999):
	for j in range(i,999):
		n=i*j
		if is_palindrome(n) and largest<n:
			largest = n
			I=i
			J=j
		
print largest,I,J,is_palindrome(906609)
