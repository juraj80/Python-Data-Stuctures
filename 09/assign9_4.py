fname=raw_input("Enter file:")
if len(fname)<1: fname='mbox-short.txt'
fhandle=open(fname,'r')
counts=dict()
emails=list()
for line in fhandle:
	line=line.rstrip()
	if line=="": continue
	words=line.split()
	if words[0]!='From':continue
	emails.append(words[1])
for name in emails:
	if not name in counts:
		counts[name]=1
	else:
		counts[name]=counts[name]+1
bigcount=None
bigemail=None
for word,count in counts.items():
	if bigcount==None or count>bigcount:
		bigword=word
		bigcount=count
print bigword,bigcount
		
		
