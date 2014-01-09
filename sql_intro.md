# Introducing SQL databases

What is a database?

What is a relational database?

## MySQL

MySQL is a popular, freely available relational database engine. There is a lot of documentation at [http://www.mysql.com] which describes hwo to interact with, manage and use the server.
Each MySQL server can support many databases. Each student will have their own database in which to work.

Each database is composed of tables, and optionally stored procedures, triggers and constraints for data processing. 

The files for this exercise can be found in the sql directory.

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

An example table for sequence information:

>	CREATE TABLE sequence (
>	id integer not null primary key,
>	accession varchar(10) not null unique,
>	created date not null,
>	description varchar(256),
>	length integer not null,
>	organism varchar(30) not null,
>	nucleotide boolean default 't',
>	gccontent double not null
>	);
	
>	describe sequence;

#### Inserting data manually

>   Insert into sequence (id, accession, created, description, length, organism, nucleotide, gccontent) 
>   values (1, 'ABC123', '2014-01-15', 'An example sequence entry', 203, 'Homo idioticus', 't', 38.7);
	

#### Inserting data from file 
reference: http://dev.mysql.com/doc/refman/5.5/en/load-data.html

If your table is a faithful representation of data in a text file (ie the columns and rows match data types and are in the right order)

>	LOAD DATA LOCAL INFILE 'sequences.txt' INTO TABLE sequence;
	
Load the sequences file into your database.	

### Querying a table


#### simple selects

#### aggregate functions (ordering, grouping etc.)

### Joining two or more tables


