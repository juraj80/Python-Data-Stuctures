counts=dict()
names=['csev','owen','csev','zqian','cwen']
for name in names:
	if name not in counts:
		counts[name]=1
	else:
		counts[name]=counts[name]+1
print counts
