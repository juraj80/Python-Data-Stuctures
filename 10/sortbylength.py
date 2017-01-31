'''example, suppose you have a list of words and you want to sort them 
from longest to shortest'''

txt = 'but soft what light in yonder window breaks'
words=txt.split()
lst=list()
for word in words:
	lst.append((len(word),word))
lst.sort(reverse=True)
res=list()
for lenght, word in lst:
	res.append(word)
print res


	
			
