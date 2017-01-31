fname=raw_input("Enter file:")
if len(fname)<1:fname="mbox-short.txt"
fhandle=open(fname)
emails=list()
counts=dict()
for line in fhandle:
	line=line.rstrip()
	if line=="": continue
	words=line.split()
	if words[0]!="From": continue
	emails.append(words[1])
for email in emails:
	if not email in counts:
		counts[email]=1
	else:
		counts[email]=counts[email]+1
bigcount=None
bigword=None
for word,count in counts.items():
	if bigcount is None or count>bigcount:
		bigword=word
		bigcount=count
print bigword,bigcount

