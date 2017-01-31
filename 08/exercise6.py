lst=[]
while True:
	inp=raw_input("Enter a number:")
	if inp=="done": break
	try:
		num=int(inp)
	except:
		"Not a number."
	lst.append(num)
print "Maximum:",max(lst)
print "Minimum:",min(lst)

