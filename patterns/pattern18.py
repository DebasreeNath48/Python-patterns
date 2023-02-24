n=int(input("enter the number of lines: "))
for i in range(1,n+1):
	for space in range(1,n-i+1):
		print(" ",end="")
	for star in range(1,(2*i-1)+1):
		if star==1 or star==2*i-1:
			print("*",end="")
		else:
			print(" ",end="")	
	print()	
for i in range(n-1,0,-1):
	for space in range(1,n-i+1):
		print(" ",end="")
	for star in range((2*i-1),0,-1):
		if star==2*i-1 or star==1:
			print("*",end="")
		else:
			print(" ",end="")	
	print()		
