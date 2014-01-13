# Piecing it all together.

We have learned many things in the last few days and now can start to put them together. When starting on a project, 
keeping it organised is key to success.

One way to organise your code and data is to use a design pattern such as the *Model-View-Controller*.

This lets us separate our datamodel, our processing code, and the representation of the data into separate units 
so they are easier to maintain. So for example we will define our data structures classes in one file. This would match 
our SQL code. These correspond to our model.  We define our web scripts  in a separate file or files so that they carry 
out functions and methods on our data objects. They will produce results (which themselves may be objects). 
The view that is put on them will be determined by the HTML pages and CSS which should be separate sections. 
Each of these can then be maintained and reused separately to the others.

Lets take a look at a hypothetical project structure:

    Project/
        README
        html/
            README
            page1.html
            page2.html
            header.html
            footer.html
            styles.css
        cgi/
        	doquery.py
        	dosearch.py
        python/
            myProject.py
            myDB.py
        db/
            database.sql
        data/
        	data.txt
        

We have separated all the aspects of our project into different directories. We include README files that explain what 
each part does and include documentation in the source codes. Our data model (the sql and python modules) just deal with the data model, we let the cgi scripts worry about querying the data model and displaying it. We use templates in the html directory to make our pages easier to maintain.

Needless to say, all of this is under revision control.