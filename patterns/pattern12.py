#alphabet pattern
n=int(input("enter the number of lines: "))
for i in range(1,n+1):
	for j in range(1,i+1):
		print("%c"%(64+j),end="")
	print()	