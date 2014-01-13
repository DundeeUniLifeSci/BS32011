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

### Sanity checking

Now we can readily take input from a user and do things to it. Consider the following form and CGI script (I've skipped some of the housekeeping bits for brevity):

    <form action=searchdb.py method=POST>
    <table><tr>
        <td>enter an SQL query</td>
        <td><input type=text name=query /></td>
    </tr></table>
    </form>
    
    
    form=cgi.FieldStorage() # get the form data from the cgi object
    cursor.execute(form['query']) # run the query on the database
    
Why is this a bad idea? [What kind of queries could be run?](http://xkcd.com/327/) Even if we restrict the user accessing the database to SELECT only, they can still write queries that take a long time and tie up resources. You should always *sanitise* input from the wide world. Check it matches what you think it should. Trust nobody.

#### Exercise:

Sanitise the input for your restriction digest program. Check the sequence title just has alphanumeric characters. Check the sequence is just ACTG. Check the restriction enzyme  name is one of the 'allowed' ones. And do this *before* you actually use any of the data.
You might find it easiest to do something like:

    cleandata={}
    try:
        cleandata['sequence']=check_sequence(form['sequence'])
        ...
    except Exception, e:
        do_error(e)
        
    def check_sequence(sequence):
        ....
        
    def do_error(error):
        '''Handles an error by putting a message in the web page'''    
        


### Templates

It can be tedious to put the same basic code into script after script. Instead we can use some form of templating 
where we only need to write the code once.

Consider the following example:

    def start_html(title, css=None):
        html="""Content-Type: text/html

    <!DOCTYPE html>
    <html><head><title>%s</title>"""%title

        if css is not None:
            html=html+"\n<link rel="stylesheet" type="text/css" href='%s'>\n"%css
        html=html+"</head>\n<body>"
        return html

We can save the method start_html() in a file (e.g. cgi_methods.py) that could be included at the start of our CGI script.

    import cgi_methods
       
    print start_html("My Page Title", "mystyle.css")          


This keeps our code cleaner and more maintainable.


This idea of templating and abstraction (where the repetitive housekeeping is managed for you) is taken further by web frameworks such as [Django](http://djangoproject.com) and [Web2Py](http://web2py.com).
