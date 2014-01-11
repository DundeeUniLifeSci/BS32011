#!/usr/local/bin/python
fh=open('numbers.txt') # open our data file
total=0 # total of numbers read so far
count=0 # count of numbers read so far
for n in fh.readlines(): # iterate through the file one line at a time
	total=total+int(n) # we read in a string so int() converts to a number
	count=count+1
fh.close()
print "%s numbers read with a total of %s"%(count, total)
