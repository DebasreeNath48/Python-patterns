n=int(input("enter the number of lines: "))
for i in range(1,n+1):
	for j in range(1,i+1):
		print("*",end = "")
	print()	
for i in range(1,n):
	for j in range(n-1,i-1,-1):
		print("*",end="")
	print()	