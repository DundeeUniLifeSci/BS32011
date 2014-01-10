# Introducing SQL databases

What is a database?

What is a relational database?

## MySQL

MySQL is a popular, freely available relational database engine. There is a lot of documentation at [http://www.mysql.com] which describes hwo to interact with, manage and use the server.
Each MySQL server can support many databases. Each student will have their own database in which to work.

Each database is composed of tables, and optionally stored procedures, triggers and constraints for data processing. 

The files for this exercise can be found in the sql directory so change to that directory before starting. Thsi is a very quick and superficial introduction to databases and SQL. There is a lot more to learn, and a lot of theory to read up on.

### Accessing MySQL

MySQL can be accessed via a command line or through a programming interface. The language used is SQL (Structured Query Language) which has an industry standard core but slight variations depending on which platform you use. These changes are minor and usually easy to transfer from one platform to another.

Your MySQL username and password will be different to your login password. Whilst in principle you could log in to a MySQL server from anywhere, the server on the teaching host is only accessible from that host.

Please note: If you are carrying out a research project rather than a teaching practical you should be using the research computing MySQL server instead.

#### From the command line
 
The program to access the server is *mysql*. You will need to give various options such as the mysql user (-u username), to prompt for a password (-p) and the database to which you wish to connect. A database has been created for you with the same name as your username.

Connect as follows:

>    mysql -u yourusername -p yourusername
	
You will be prompted for a password which you will have been given.

If all goes well youshould end up at a prompt which looks like

>    mysql>

At the moment you have nothing there. To see the tables which have been defined, use the command

>    show tables;

Note how the command is terminated with a semicolon (;).

### Creating a table
[reference: http://dev.mysql.com/doc/refman/5.5/en/creating-tables.html](http://dev.mysql.com/doc/refman/5.5/en/creating-tables.html)

We will create a table to store sequence information. 
The information we need to save is:

A unique index for each entry
Accession number
Date it was created
Description
Length
Organism
Type (nucleotide or protein)
GC content.

When we define a table we state the type of information that is in each field.

##### Exercise:
Determine which type of data should be in each field.
[reference: http://dev.mysql.com/doc/refman/5.5/en/data-types.html](http://dev.mysql.com/doc/refman/5.5/en/data-types.html)


##### An example table for sequence information:

	CREATE TABLE sequence (
	id integer not null primary key auto_increment,
	accession varchar(10) not null,
	nucleotide enum('N','P'),
	length integer not null,
	gccontent float not null,
	description varchar(256),
	organism varchar(50) not null
	);
	
	describe sequence;
	
###### What do all these mean?
* We create a table with the name *sequence*
* *id* is an *integer* that cannot be null, it is the *primary key* so must be unique and if it isn't specified then we can automatically generate it by *auto_increment* from the previous highest value.
* *accession* is a text value (maximum length ten characters) that cannot be null (empty).
* *nucleotide* is either the value 'N' or the value 'P' (any one of the list of values in the enum)
* *length* is an *integer* (whole number)
* *gccontent* is a decimal (floating point) number
* *description* is a text field of max size 256
* *organism* is a text field of max size 50


#### Inserting data manually

   Insert into sequence (id, accession, nucleotide, length, gccontent, description, organism) 
   values (1, 'ABC123', 'N', 23,65.3,'a test sequence', 'a test organism');

Note that the text is between quotes but the numbers are not.
   
#### Inserting data from file 
[reference: http://dev.mysql.com/doc/refman/5.5/en/load-data.html](http://dev.mysql.com/doc/refman/5.5/en/load-data.html)

If your table is a faithful representation of data in a text file (ie the columns and rows match data types and are in the right order)

	LOAD DATA LOCAL INFILE 'seqinfo.txt' INTO TABLE sequence 
	IGNORE 1 LINES
	(accession, nucleotide, length, gccontent, description, organism);
	
Load the sequences file into your database.	Note that the sequence file has no ID so we have to specify the fields into which we want to load the data, and that we tell it to ignore 1 line at the top of the file.


### Querying a table

[reference: http://dev.mysql.com/doc/refman/5.5/en/retrieving-data.html](http://dev.mysql.com/doc/refman/5.5/en/retrieving-data.html) 
The key way to select data from the database is the _SELECT_ statement where we specify:

    SELECT what
	FROM which_table
	WHERE conditions
	
	

#### simple selects
Example:
	SELECT accession FROM sequence;

This selects all the accessions from the sequence table - we see that it has returned a large number of rows.

    SELECT accession, length, gccontent FROM sequence WHERE accession='ECs0003';

This selects the fields *accession*, *length*, *gccontent* from all the entries whose accession matches 'ECs0003' - this should be just one entry.

    SELECT accession, length, gccontent FROM sequence WHERE length < 90;

Maybe we want to see what types are available, e.g. which organisms are in our database?
    SELECT DISTINCT organism from sequence;
	
We can also do wild card matching:
	SELECT * FROM sequence WHERE accession LIKE 'rr%';

The % matches any sequence of characters and up to two % can beused in any one LIKE statement.

There are many more
	
#### aggregate functions (ordering, grouping etc.)

SQl supports aggregate functions which are procedures or calculations carried out over multiple sets of data. 
Examples of these are _min()_, _max()_, _count()_ and so on.

How many sequences have a length longer than 1000nt?

    SELECT count(*) FROM sequence WHERE length >1000;

Calculate the average length:
	SELECT sum(length)/ count(length) AS average FROM sequence;
	
Note hwo we change the output field name with _AS_;

We can also calculate over groups:

    SELECT organism, sum(gccontent)/count(gccontent) as 'Mean GC content' FROM sequence GROUP BY organism;
	

### Joining two or more tables

First we need more tables. The file _expression.tab_ is a table of some expression data from an experiment on one of the organism. The file has several fields - the gene name, the expression value, and the experiment. We will create a new table that links to the existing sequence table, then load in the data.

To link data we can specify a field in our new table that references a row in another table. This is known as a _FOREIGN KEY_. The target field must be _NOT NULL_ and _UNIQUE_. It can be a text field or an integer - I prefer to use integers as then we can use _AUTO_INCREMENT_ to create the index automatically. The field we will link to is _id_ in _sequence_.

    CREATE TABLE expression (
	sequence integer not null,
	FOREIGN KEY sequence REFERENCES sequence (id),
	-- this links this table to our sequence table.
	expression INTEGER NOT NULL,
	experiment VARCHAR(20) NOT NULL
	);
	
There is a more complicated LOAD INFILE statement. This does a lookup to determine what the ID value should be. Don't worry about understanding the mechanics of this right now.
    
#TODO

### Deleting data

We can delete individual rows with the _DELETE_ statement. ___CAUTION: This is dangerous if misapplied___

    DELETE FROM sequence WHERE accession='ABC123';

If the WHERE clause is not specified it will delete all matching rows (ie all).

You will get an error if you try to delete a row which is the subject of a FOREIGN KEY reference. Ie if that data is referred to then deleting it would cause inconsistency in the database so that is not allowed. 

To delete a table or other object, use _DROP_

    DROP TABLE sequence;
	
Hopefully this will give an error as the table _sequence_ is referred to by the table _expression_. You can't DROP TABLE sequence until you have done DROP TABLE expression to remove the referring table.