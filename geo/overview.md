# Planning your project

## First steps

Create a new directory and initialise a git repository there to keep your work under version control.

Create a README.md file to describe your project and what the various bits of your code do.

## Getting data

Go to the [Gene Expression Omnibus](http://www.ncbi.nih.nlm.gov/geo) and find a dataset that interests you. Maybe it is a cancer study, maybe cell signalling. The choice is entirely yours. It would be a good idea to limit yourself to single channel experiments that are not too complex.

Download the data as described in the [introduction to GEO data](introducing_geo.md)

### Write a parser for the GEO datafile

This should read your dataset and represent it electronically. [Some notes on parsers](parser.md)

### Plan your database

Look at the data you have downloaded and decide how to represent it in the MySQL database. You may find it helpful to use diagrams like [entity-relationships](http://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) or 
[UML class diagrams](http://www.ibm.com/developerworks/rational/library/content/RationalEdge/sep04/bell/) (the link gives one view, skim through and look at the diagrams before reading in detail).

The class diagrams can also help you think about the methods you want to attach to your classes.

### Create your object models

This is the set of python classes that you will use to represent your data (gene, experiment etc), and the SQL that describes your database (the CREATE TABLE commands you use to build it).

### Modify your parser

This should read your dataset and now put it into the database.

### Plan the web interface

What questions do you want the user to be able to ask? What database queries will those require?
Test the queries so you know they give you the results you expect.

### Design your web page

How will it be laid out? Which classes do you need for your HTML elements? Which form pages do you need?

### Write the CGI scripts

Now you have to take the input from the web pages, query the database and return the results.


## Process

As you carry out these steps, record your decisions in a README file. e.g.
Bear in mind that you won't be able to achieve everything you wish. The aim of the practical project is to get technical competence. 

	Database design
	I have decided to not capture GO terms as that would require another layer of tables and be too complex for now. 

### code sharing/discussion

I expect you will discuss this amongst yourselves, that is great. If you wish to reuse someone elses code then that is fine but the following two things must be observed:

1. You can explain what everything in the code does.
2. That block of code is clearly marked with comments that state who the author was.

### Version control.

Commit early, commit often. If you want to ask me questions about your code I will look for it in your git repository.


### Documentation

Every file should have a description of what it contains. For HTML this will be a comment between tags like

    <!-- an HTML comment -->
    
For python it will be docstrings or comments - every method and class should have a docstring that says what the method does.

For SQL start comment lines with --

For CSS use comments in blocks like 

    /* a comment */
    
Don't forget to include your name in a comment/documentation in each file.

