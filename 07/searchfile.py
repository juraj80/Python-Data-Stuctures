fhand=open('mbox-short.txt')
for line in fhand:
	line=line.rstrip() #striping /n from file
	if line.startswith('From:')
		print line

