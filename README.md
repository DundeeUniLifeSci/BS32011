# 3rd Year Bioinformatics practical

## Aims

1 To develop the practical skills required to effectively implement bioinformatics workflows and data analysis. 
1 To develop understanding of how to work collaboratively on data analysis 
1 to understand provenance and sustainability in bioinformatics analysis
	
## Structure

The practical will consist of two parts. The first part is an intensive refresher on Python. We will also introduce using version control with git so you will need to create for yourselves a github account (http://github.com) before the first session.

To get a refresher in Python before the practical starts, you can work through some of the on-line courses, eg [http://pythonforbiologists.com] (you will need to register to get the data files for the examples - it is free) or [http://trypython.org]


Over the course of the project we will 
* Retrieve some gene expression data from GEO, 
* write a script that will process it into a suitable form. 
* Place it into a relational database. 
* Write a web script that can retrieve and display the data and set it up as a web server.
	
We will record our progress using version control and document our code well.

## Working platform
We will use the Scientific Computing Lab. This is a virtual environment where we can log in to a remote desktop. A copy of this environment will be available as a virtual machine so you can install it on your own machine(s). You'll discover how easy it is to keep these in sync using git/Github.

## Project timeline
### Lab meetings
Initial introductory sessions will be Monday 19th January 12-3pm, Wednesday 21st 10-1, and Thursday 22nd 11-2 and 3-6pm. 
You are expected to work outside these hours - the contact time is to help you get up to speed with the nature of the practical.

Following the introductory week, lab meetings will be from 12.00-13.00 on Wednesdays in Tower IT suite B from week 16 (28th Jan)-Week 19

Timelines are as follows with week by week deliverables noted. Deliverables should be tagged in your GitHub repository.

### Week 1 - Python revision and getting started
* [Setup and Introduction](setup.md)
* [Using Unix](shell/README.md)  
* [Python revision - variables and files](python/python_files.md)
* [Python regular expressions](python/python_regexp.md)
* [Python methods](python/python_functions.md)
* [Python classes](python/python_classes.md)
* [Documentation](python/python_documentation.md) and [testing](python/python_testing.md)
* [Data and code sharing with git](git/README.md)
* [Select and download data from GEO](geo/overview.md)
* [Writing a parser for the data to extract it from the raw download.](parser.md)

_Deliverables:_ Dataset from GEO. Parsing script that can extract the data into appropriate variables. 

### Week 2 - Storing our data in a database
* [Relational databases (MySQL)](sql/sql_intro.md)
* [Python and relational databases (MySQLdb)](sql/sql_python.md)
* By the end of this week you should have designed the database tables and imported the data. 

_Deliverables:_ SQL Schema. Script to extract data from the raw file and prepare it for insertion into the database as SQL statements.

### Week 3 - Using Python to retrieve data from MySQl
We will write Python functions that can query the relational database, returning the results in an appropriate data structure. This will be put together in a module.

_Deliverables:_ A python class or classes that contains methods to retrieve entries in an appropriate data structure from the SQL database.

### Week 4  We will learn how to build a web form and structure a web page. This will be set up on a web server.

* [HTML](cgi/html.md) and [CSS](cgi/css.md)
* [CGI forms](cgi/forms.md)
* [Python and CGI](cgi/python_cgi.md)

_Deliverables:_ A web page that demonstrates the use of appropriate formatting with CSS and a form that interacts with the server as demonstration CGI code

### Week 5
Integration of the web form with the SQL database so that queries made via the web form can be returned as a web viewable result.

_Deliverables:_ The final finished web site that allows the data downloaded from GEO to be interrogated via a web form.


## Assessment of lab books

In this practical your Git repository is your lab book. 
The [guidelines](labbook.md) explain what is expected of a repository.