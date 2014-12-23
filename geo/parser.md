# Writing a parser

The role of a parser is to read a data file and extract the necessary information into a form that we cna manipulate in a computer. Each data format will require a different parser. Some are easy to write, and others more complex if there is a complex data model.

You will have decided already on the data strcuture (ie Gene, probe, experiment and how they relate to one another). The role of the parser is to turn the data encoded in the GEO download, into our object so they can be stored in the relational database.

1. Look at the data file. How is the information structured? 
2. Think about how you will represent the data when you read it. Will you store lists of genes/expreiments as arrays or dictionaries?
3. reading in the data: Do you want to skip all lines until one that matches a certaincriterion?
4. How do you process each useful line.
5. How do you know when you have reacehd the end of the data?

An outline parser script can be found [here](readdata.py). This is incomplete and requires completion and the addition of appropriate documentation.

In the first instance we will get the parser to read in the data in which we are interested. Once we are happy it can do that we can modify it to upload data into the SQL database.
