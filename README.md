# 3rd Year Bioinformatics practical

## Aims

1 To develop the practical skills required to effectively implement bioinformatics workflows and data analysis. 
2 To develop understanding of how to work collaboratively on data analysis 
3 to understand provenance and sustainability in bioinformatics analysis
	
## Structure

The practical will consist of two parts. The first part is a 3 day overview where you will be introduced to the techniques and concepts that you will be using. This is a very rapid 'crash course' or 'bootcamp' and should be supplemented with your own reading and practice. The material was originally intended to take a class through 'en bloc' but scheduling prevents that so you will have to work through it in your own pace. It should take you about three working days to complete. I will be available all day Monday, Thursday and Friday during the first week to assist with any queries. You will not be expected to remember everything you need for part 2, but you will have been introduced to the concepts and know where to find out the details. 

The second part is the practical exercise where you will put these skills into practice in your own time. 7 full working days have been allocated for the second part, and you can complete this at your own schedule.

*This is a work in progress. The documentation on these pages will be updated periodically.*

## Part 1: Bootcamp you should aim to complete this by the end of the first week.

### Day 1


* [Setup and Introduction](setup.md)
* [Using Unix](shell/README.md)  
* [Python revision - variables and files](python/python_files.md)
* [Python regular expressions](python/python_regexp.md)
* [Python methods](python/python_functions.md)
* [Python classes](python/python_classes.md)

### Day 2 
* [Documentation](python/python_documentation.md) and [testing](python/python_testing.md)
* [Data and code sharing with git](git/README.md)
* [Relational databases (MySQL)](sql/sql_intro.md)
* [Python and relational databases (MySQLdb)](sql/sql_python.md)

### Day 3
* [HTML](cgi/html.md) and [CSS](cgi/css.md)
* [CGI forms](cgi/forms.md)
* [Python and CGI](cgi/python_cgi.md)
* Piecing it all together - Model, View, Controller
	
## Part 2: Exercise

You will download a gene expression dataset from a public database (eg GEO). The choice of dataset is up to you but should be confirmed with Dr Martin.  You will construct a suitable database structure to hold it, and provide a web interface to allow a user to interrogate that data (filter/select specific data by criteria you determine) which will then be presented as a web page. Your code should be fully documented and in revision control. You should show good separation between data structures (model), Data representation to the user (view) and the program code that controls this (controller).  
