fhand=open('mbox-short.txt')
for line in fhand:
	line=line.rstrip() 
	if line=='': continue
	words=line.split()
	#print words
	#if words==[]: continue    #guardian pattern always put before question
	if words[0] != 'From': continue
	print '=======',words[2]

