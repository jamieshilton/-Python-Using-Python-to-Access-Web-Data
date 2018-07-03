import re

fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "regex_sum_189548.txt"
numlist = list()

fh = open(fname)

for line in fh:
    line = line.rstrip()
    numb = re.findall('[0-9]+', line)
    if len(numb) >= 1:
        for n in numb:
            num = int(n)            
            numlist.append(num)
    
print "Sum:", sum(numlist) 
