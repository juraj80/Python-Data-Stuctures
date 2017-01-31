handle=open("romeo.txt")
counts=dict()
for line in handle:
	words=line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1
tmp=list()
for k,v in counts.items():
	tmp.append((v,k))
tmp.sort(reverse=True)
for k,v in tmp[:10]:
	print v,k
	
			
