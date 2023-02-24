n = int(input("enter the number of lines: "))
for i in range(n,0,-1):
	for space in range(1,n-i+1):
		print(" ",end="")
	for star in range(1,2*i):
		print("*",end="")
	print()		
for i in range(1,n+1):
	for space in range(n-i,0,-1):
		print(" ",end="")	
	for star in range(1,2*i):
		print("*",end="")
	print()		