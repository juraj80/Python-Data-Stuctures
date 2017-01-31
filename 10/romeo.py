''' print the ten most common words in the text '''
import string
handle=open('romeo-full.txt')
counts=dict()
for line in handle:
	line=line.translate(None,string.punctuation)
	line=line.lower()
	words=line.split()
	for word in words:
		if not word in counts:
			counts[word]=1
		else:
			counts[word]=counts[word]+1
res=list()
for k,v in counts.items():
	res.append((v,k))
res.sort(reverse=True)
for k,v in res[:10]:
	print v,k

