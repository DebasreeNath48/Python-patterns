n=int(input("enter the number of lines: "))
for i in range(1,n+1):
	for space in range(1,n-i+1):
		print(" ",end="")
	for star in range(1,i+1):
		print("* ",end="")
	print()		