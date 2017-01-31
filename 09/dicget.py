counts=dict()
names=['csev','owen','csev','zqian','cwen'] 
for name in names:
	if name not in counts:
		counts[name]=1
	else:
		counts[name]=counts[name]+1
print counts


# print counts.get(name,0)
#equals
#if name in counts:
#	return counts[name]
#else:
#	return 0

#counts=dict()
#names=['csev','owen','csev','zqian','cwen'] 
#for name in names:
#	counts[name]=counts.get(name,0)+1
#print counts

