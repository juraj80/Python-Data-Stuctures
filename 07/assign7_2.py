fname=raw_input('Enter file name:')
fhandle=open(fname)
count=0
total=0
for line in fhandle:
	if not line.startswith('X-DSPAM-Confidence:'): continue
	line=float(line[-7:])
	total=total+line
	count=count+1
print 'Average spam confidence:',total/count 
	
