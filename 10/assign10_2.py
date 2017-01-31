'''10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages. You can pull
the hour out from the 'From ' line by finding the time and then splitting 
the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below.
'''

name=raw_input("Enter file:")
if len(name)<1: name='mbox-short.txt'
handle=open(name)
t_list=list()
for line in handle:
	line=line.rstrip()
	if not line.startswith('From '): continue
	words=line.split()
	t_list.append(words[5])
h_list=list()
for item in t_list:
	item=item.split(":")
	h_list.append(item[0])
counts=dict()
for hour in h_list:
	if not hour in counts:
		counts[hour]=1
	else:
		counts[hour]=counts[hour]+1
#for hour in h_list:
#    counts[hour]=counts.get(hour,0)+1 #in one line		
tups_list=counts.items()
#tups_list=sorted(tups_list)
#tups_list=sorted(counts.items())  #in one line
tups_list.sort()

for k,v in tups_list:
	print k,v
# for k,v in sorted(counts.items()): #in one line
	
	

