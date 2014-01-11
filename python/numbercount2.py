#!/usr/local/bin/python
fh=open('numbers.txt') # open our data file
total=0 # total of numbers read so far
count=0 # count of numbers read so far
skipped=0 # number of bad data points
for n in fh.readlines(): # iterate through the file one line at a time
	try:
		total=total+int(n) # we read in a string so int() converts to a number
		count=count+1
	except:
		print "Bad data %s - skipped"%n.rstrip() #take off the newline at the end of the string.
		skipped=skipped+1
fh.close()
print "%s numbers read with a total of %s. %s skipped."%(count, total, skipped)