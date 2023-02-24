n=int(input("enter the number of lines: "))
for i in range(1,n+1):
	for space in range(1,n-i+1):
		print(" ",end="")
	for star in range(2*i-1):
		if star==0 or star==2*i-2:
			print("*",end="")
		else:
			if i==n:
				print('*',end="")	
			else:	
				print(" ",end="")
	print()			