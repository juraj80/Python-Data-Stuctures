fname=raw_input('Enter a file name:')
try:
	fhandle=open(fname)
except:
	print 'File cannot be opened:',fname
	exit()
count=0
for line in fhandle:
	if line.startswith('Subject:')
		count=count+1
print 'There were',count,'subject lines in',fname


