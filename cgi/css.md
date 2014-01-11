# Making it look pretty the easy way - adding style to your web page.

So far the web pages we have produced have been pretty industrial. They are very basic and not always effective at 
presenting the information we wish in the way we wish it.

Styles allow us to control the look, feel, visibility and many other aspects of our web pages. They are a powerful way
of allowing us to control the presentation of information in a way that best communicates with the reader/viewer.
 
There are very good introductions to styles on the web, particularly [at the w3c](http://www.w3.org/community/webed/wiki/CSS/Training) which you should read and work through after reading these brief notes. 


### Adding styles to an element

The old school way of adding style was to use attributes that were specifically included in the tag definition. For 
example a *body* tag coul dallow you to specify the background colour and font colour as follows:

    <body color='#0000FF' bgcolor='#FFFFAA'> ... some content ... </body>
    
which should give a rather hideous blue font on cream background. The problem was that this required a lot of definitions in the tag and was rather unwieldy. Instead we can use styles defined in one of three places.

1 In the tag. We add a *style='...'* attribute to the tag and put the definitions in there. This is fine for one-off 
definitions but awkward if we want to make lots of changes.
2 As an inline style definition in the document. We define rules for the whole document in a block in the header. Fine if you are just managing one document but awkward if you need to maintain many documents.
3 As a separate file which contains the definitions for the whole site. This is the easiest to maintain and the best in terms of separating content from display

In practice we will use combinations of all three. The rules read from external files are overwritten by rules that are embedded in the document. And rules written in the tag itself override all others.

#### Reading a style sheet from a file

In the *head* section add a line like the following:

     <link rel="stylesheet" type="text/css" href="style.css">

The URL can be relative, absolute or fully qualified. If you read several files the definitions in the later files will 
supercede those in the earlier files. 

#### Embedding a style sheet

Again, in the *head* section you can include a *style* block which contains your style definitions

    <style>
      h1 {color: #00FF00; font-size: 200%}
    </style>

Add this to your index.html file and note the results.

#### Applying style rules to an element

We can do this by adding a *style* attribute containing the rules to the tag. For example, adding this into a 
web page should illustrate the point.

    <p style="color: red; font-weight: bold;">This should be bold red text</p>     
    
### Style sheet rules

Style sheet rules are a simple format. They take the rule name, a colon (:) and the definition. Each rule is separated 
from the next with a semicolon (;). Rules are enclosed in braces {} and appear after the nmae of the element to which 
they apply.

    div {color: blue; align: right;}
    p {color: black; align: left;}
    h1 {color: green;}
    
and we apply the style to this document fragment:

    <div>
      <h1>A big title</h1>
      <p>Some text to read</p>
      <h2>A smaller title</h2>
      <p>Some more text to read</p>
    </div>

When applying rules the browser will cascade upwards till it finds a rule to work with. For example it has a rule for colour for the paragraph so it applies that (red). It however doesn't ahve a rule for colour for *h2* so it looks at the next element out which is *div*. *div* has a rule for colour so it applies that.

The element name is known as the *selector* and it can become quite complex as we shall see shortly.

#### Exercise: 

Copy the file */BS32011/cgi/results.html* to your home directory. Look at it in a text editor and add a reference to 
an external css file *results.css*.  

Create the file *results.css* and set format rules for the web page. You shouldn't have to do much typing here - specify rules for each element type and use cascading as much as possible as they will inherit.

#### Classes and individual elements in style sheet rules.
[reference: http://www.w3.org/community/webed/wiki/CSS/Training/Selectors](http://www.w3.org/community/webed/wiki/CSS/Training/Selectors)


So far we have treated every element of a type (e.g. all *div*) the same. We can assign elements to different groups (known as classes) and apply different rules to those classes. An element can be in more than one class and a class can contain more than one type of element.

Let's take for example that we want to produce a warning message and want it in bright red. Our web page may have many warnings on it so we want to define the style in one place.

    <div>
        This is some normal text.
        <div class='warning'>
        	Appearances can be deceptive
        </div>
        Really, it is just normal text.
    </div> 
    
And a style sheet for this 

    body {color:black;}
    .warning {color:red;}
    div.warning {border-color: red; border-width: 1px;}
    
Note the .classname syntax where a fullstop precedes the class name All the text that is not in the class warning will be black, but text inside an element of class warning will be red. In addition a div of class warning (or inside a div of class warning that dosn't have a specific alternative rule - see the section on cascading above) will have a red box around it.

Classes are really useful for displaying different data in different ways. With some simple javascript elements can have classes added and removed, and the display properties of elements can be changed dynamically (e.g. those pop-up info boxes or survey boxes when you visit a web page)

Individual elements are specified with the syntax *id=identifier* in the opening tag of the element. Only one element should have a particular id.

To specifiy the rule for an individula element use the syntax:

    #id {rules}
    
e.g.
	
	<div id='pagebody'>
		<h1 id='pagetitle'>This is the page title</h1>
	</div>
	
could have the CSS

	#pagetitle {format rules for page title}	
	
Identifiers and classes can be used in combination to get very fine grained control over elements and groups of elements.

#### Exercise: 

Take *results.css* and modify it to format the good hits (class goodhit) differently to the fair hits (class fairhit) and the poor hits (class poorhit). Highlight the top hit separately (id=hit1)

Place the summary info into a box with a border. Make sure there is sufficient space (padding) inside the box.

You will need to refer to the online documentation for this.


 