# Accessing MySQL databases from Python
[reference: http://mysql-python.sourceforge.net/MySQLdb.html](http://mysql-python.sourceforge.net/MySQLdb.html)

The module we use to allow Python to talk to the MySQL database is <code>MySQLdb</code>

    import MySQLdb

#### Creating a connection	
In order to access the database we create a *connection* object that contains teh details of where the database is (the host), 
the user that is accessing the database, the database name and the users password so it can log in. By default the code will assume 
the username of the person running the code, and that the MySQL database is on the local machine and the standard port.

	db=MySQLdb.connect(db="mydatabase", user="dbuser", passwd="mypassword")
	
	
####Running a query

So that is a connection. In order to run a query we need a *cursor*.

    cursor=db.cursor()
	accession = "ECs0034"
	cursor.execute("SELECT accession, length, gccontent FROM sequence where accession = %s", (accession,))
	
Two things here should be noted. 
1 The module sql parser takes a list (as a tuple) of arguments to substitute into the point where it says %s and will automatically put the necessary quotes etc round it so you don't have to. 
2 The tuple should be of at least two elements or have a comma at the end so Pythonsees it as a tuple and not a single value.

##### Why substitute into an SQL command? 

This allows us to write one command and reuse it with many values. This reduces errors and makes maintaining the code easier.

#### Retrieving results

We can retrieve results with the commands *fetchone()*, *fetchmany(n)*, and *fetchall()*

    result=cursor.fetchone()
	result
	
You should see that the result is an array of the fields. *fetchmany(n)* and *fetchall()* return an array of arrays.

	n_req=10 # just want to retrieve the top ten hits
    cursor.execute("select accession, length from sequence where length >1000 order by length desc")
    result=cursor.fetchmany(n_req)
    print "retrieved top %s hits"%len(result)
    for r in result:
        print "%s\t%s"%(r[0],r[1])
		
		
### Exercise:

Write a python script that will print the average lengths of the twenty most GC rich and the 20 most AT rich sequence from your database.