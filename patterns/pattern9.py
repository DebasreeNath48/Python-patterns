n=int(input("enter the number of lines: "))
for i in range(n,0,-1):
	for space in range(1,n-i+1):
		print(" ",end="")
	for star in range((2*i-1),0,-1):
		print("*",end="")
	print()		
