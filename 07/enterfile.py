inp=raw_input("Enter a file:")
try:
    file=open(inp)
except:
    print "Error. Please Enter a File."
    exit()
for line in file:
    line=line.rstrip()
    print line

