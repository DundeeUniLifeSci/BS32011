#Processing CGI queries with python

## What is CGI?

CGI is the Common Gateway Interface, a standard way for browsers and web servers to pass information back and forth. Most programming languages and web servers contain support for CGI that hides the gory details and makes the values accessible to the programmer in an easy way.

Values are made available as a series of key=value pairs (one for each form element) which is why you need to use unique
values for the element names. To avoid confusion (what if you want an = in your value?) the data is encoded when sent 
from the server and decoded before you get it.

## Python and CGI.

Python handles cgi with the *cgi* module. It also has the helpful *cgitb* module which turns on smarter error reporting (very useful for debugging).

A simple python CGI script:

	#!/usr/local/bin/python
	import cgi
	import cgitb
	cgitb.enable()
	
	form = cgi.FieldStorage()
	
	print "Content-Type: text/html"     # HTML is following
	print                               # blank line, end of headers
	print "<html><head><TITLE>CGI script output</TITLE></head>"
	print "<body><H1>Form values</H1>"
	print "<table><tr><th>Key</th><th>Value</th></tr>"
	
	for k in form.keys():
	        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k])
	
	print "<table>"
	
	print "</body></html>"

Things to note in this script:

* Anything printed to stdout is sent back as a response.
* We initialise the cgi and cgitb modules, and enable debugging.
* The values sent from the web server can be extracted with the *FieldStorage()* to a dictionary.
* HTTP always starts with a request/response header followed by a blank line. This includes the 
information about the type of information being sent/returned 
* After the blank line we send our page content (in HTML)
* We can reference the relevant field directy in the dictionary returned by *FieldStorage()* (but we need to know it's name)

### Exercise

1. Save this script as *formtester.py* in your *~/public_html/cgi-bin/ directory. Set the *action* for your web form to point to this script (http://ts-ug-dev/lifesci.dundee.ac.uk/~USERNAME/cgi-bin/formtester.py) and then fill in and submit the form. 

2. Create a new CGI script that can handle your restriction enzyme data. It should calculate and return the length 
of the sequence and a list of all the sites that match the restriction pattern. 




