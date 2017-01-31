name=raw_input("Enter file:")
if len(name)<1: name='mbox-short.txt'
handle=open(name)
times=list()
for line in handle:
	line=line.strip()
	if not line.startswith("From "):continue
	words=line.split()
	times.append(words[5])
hours=list()
for xtime in times:
	xtime=xtime.split(":")
	hours.append(xtime[0])
counts =dict()
for hour in hours:
	if not hour in counts:
		counts[hour]=1
	else:
		counts[hour]=counts[hour]+1
t=counts.items()
t.sort()
for k, v in t:
	print k,v

