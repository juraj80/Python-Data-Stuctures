fname=open('mbox-short.txt')
for line in fname:
	line=line.rstrip()
	if line=="":continue
	words=line.split()
	if words[0]!='From': continue
	print words[1]
	
