fname=open("romeo.txt")
lst=[]
for line in fname:
	line=line.rstrip()
	words=line.split()
	for word in words:
		if not word in lst:
			lst.append(word)
	lst.sort()
print lst
	
