name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails=list()
for line in handle:
    line=line.rstrip()
    if line=="":continue
    if not line.startswith("From:"):continue
    words=line.split()
    emails.append(words[1])
counts=dict()
for email in emails:
    if not email in counts:
       counts[email]=1
    else:
        counts[email]=counts[email]+1
print counts
bigcount=None
bigemail=None
for email,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigemail=email
print bigemail,bigcount
