inp=raw_input("Enter a file:")
try:
	fhand=open(inp)
except:
	print "Error. Enter a file."
	quit()
for line in fhand:
	line=line.rstrip()
	print line

