fhandle=open('mbox-short.txt')
for line in fhandle:
	line=line.rstrip()
	#skip uninteresting lines
	if not line.startswith('From:') # if not 'From:' in line:
		continue
	#process our interesting line
	print line
	
