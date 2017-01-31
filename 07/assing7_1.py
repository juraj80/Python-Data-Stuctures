fname=raw_input('Enter file name:')
fhandle=open(fname)
for line in fhandle:
	print line=line.rstrip().upper()
	
	
