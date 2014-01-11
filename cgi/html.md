# Introducing web pages

##The web request

When you use your web browser (or any other program that uses the web) it sends a *request* across the network to a *server* asking for a specific *document*. This request may also include additional information (such as from a web form) but in this first instance we will consider simple documents. The request specifies a Uniform Resource Identifier (or Unifor Resource Location), the URI or URL you may have seen mentioned.

An example URI:

    http://ts-ug-dev.lifesci.dundee.ac.uk/BS32011/README.md

The *http://* specifies the *protocol* (in this case the *Hypertext transfer protocol* which is	the standard for information on the web.

The  *server* address is *ts-ug-dev.lifesci.dundee.ac.uk* - this is the machine from which the client is requesting the resource.

The actual *resource* is found at /BS32011/README.md. This web server is located on the teaching lab machine so you might be tempted to look for /BS32011 in the directory structure. It is not there. The server configuration specifies where the documents can be found. They may be in a number of different locations or even on different machines.

Server configuration is mostly beyond the scope of this practical - it is all set up for you. This is only a brief introduction to the web. There is much, much more that can be learned. In particular we are not covering [accessibility](http://www.w3.org/WAI/) which is very important for ensuring that all can access the information you present or [dynamic web pages](http://w3c.org/standards/webdesign/script) which allow you to have interactive and responsive pages using javaScript libraries such as [JQuery](http://jquery.com) and [D3](http://d3js.org) for data visualisation. You are strongly encouraged to look at these when you have mastered the basics of HTML/CSS and CGI.


### Creating a first web page.

In a terminal, navigate to your home directory. Then create a directory *public_html* (it must be spelled exactly like that)

    $ cd ~
	$ mkdir public_html
	$ cd public_html
	$ nano index.html
	
We are creating a web page so enter the following (adjusted to match your particular details).

    <!DOCTYPE html>
	<html>
	    <head>
		    <title>David's home page</title>
		</head>
		<body>
		    <h1>David's Home Page</h1>
			Hi, I'm Dr David Martin and this is my home page. I am responsible for the BS32011 bioinformatics practical where we are learning the skills needed to manage and display biological data.
		</body>
	</html>
	
Save this file (it is called *index.html*) and point your web browser to http://ts-ug-dev.lifesci.dundee.ac.uk/~yourusername/index.html and you should see your page.

### The structure of web pages
[reference: http://www.w3schools.com/html/](http://www.w3schools.com/html/)

HTML (Hypertext markup language) is the standard language used to describe page layout and content. It is a variant of XML (eXtensible Markup Language) which is a hierarchical tag based language. The whole page is placed between a pair of tags 

    <html> ... </html>
	
Each section is then held within it's own set of tags. There is a header which contains setup information and the title of the page (used in bookmarks and in the titlebar of the browser window.)

    <head> ... </head>
	
and a body that contains the content which will be displayed

    <body> ... </body>
	
You have seen already that we put  some text between tags and got a big title 

    <h1>title text here</h1>
	
Each set of tags is of the form 
     <tagname *parameters*> ... content ... </tagname>
There are many other types of *element* that we can use and they will be introduced in due course. Elements are *always nested* and *never intersect.*

    <outer> ... <inner> ... </inner> ... </outer>

is valid but

    <left> ... <right> ... </left> ... </right>
	
is not permitted.

Elements used for text layout are classified as BLOCK or INLINE depending on how the behave. Every element can take parameters that control it's behaviour. We'll cover these by example as we go.

### Block elements

A block level element is one which acts as a completely separate block. By default it will occupy the full width of the screen so it starts immediately vertically after the preceeding block when the page is laid out and the following block will start immediately vertically after it. It is a box on the screen.

All the headings *h1, h2  ... h6* are block elements. The most common one is *div* which is an arbitrary block container. Free text is by default put into a *p* container (paragraph). You can try the effect of the p container as HTML layout ignores newline and extra whitespace.

	<h1>One paragraph</h1>
	This text is formatted as one paragraph
	
	even though we have put a blank line in between.
	<h1>Two paragrpahs</h1>
	<p>This text will be formatted as two paragraphs.</p>
	<p>It will not be wrapped because the paragraph element is a block element</p>
	
### Inline elements

Inline elements run inline to the context in which they are found. They will not force a new line or any particular spacing. The canonical element is *span* which is an arbitrary chunk of text. More specific ones for formatting text are *em* for emphasised (italic), *i* which is also italic and *b* for bold. The link element *a* is also an inline element.

    This text has <i>italic and <b>bold italic</b></i> <em>formatting</em> inline.

#### Exercise:
Update your home page with some more text. Ensure it is formatted into paragraphs, headers and uses bold and italic as appropriate.
	
### Lists

A list is a block level element. HTML supports three types of list:

* Unordered list - this is a set of bullet points.
* Ordered list - this is a numbered list of items.
* Definition list - this has a term and a definition for each element.

#### Ordered and unordered lists.

An ordered list uses the tag *ol* and an unordered list has the tag *ul*. Each list item is between *li* and */li* tags.

    <ol>
	    <li>Item number one</li>
	    <li>Second item</li>
	<ol>
	<ul>
	    <li>A point in an unordered list</li>
	    <li>Another point</li>
	</ul>
	
Lists can be nested:

	<ul>
		<li>the first point</li>
		<ul>
		    <li>a sub point</li>
		</ul>
	</ul>

#### Exercise:

Add a list to your home page. It could be a list of books you have read, or hobbies you participate in.
	
### Links

Links are specified using the *anchor* tag which has the tag nema *a*.  It requires that you specify either a name for the anchor, or the URI for the link. The part between the *a* tags is the bit which is highlighted so you can click on it.

    <a href='anotherpage.html'>Click here to go to another page</a>
	<a href='/BS32011/README.md'>The bioinformatics practical home page</a>
	<a href='http://google.com/'>Search for something</a>
	
Links have an href attribute (parameter) which can be specified in several ways. The first one above is a relative path. It looks in the same location on the server for a page called 'anotherpage.html'. If you had pointed your  browser at your home page on *http://ts-ug-dev.lifesci.dundee.ac.uk/~username/index.html* and it contains the above link, then it would look for the page *http://ts-ug-dev.lifesci.dundee.ac.uk/~username/anotherpage.html*

By contrast, if the page contained the second link, this is an absolute path (to */BS32011/README.md* ) so it would look for that page reference starting at the server root. This is not so protable if you move your pages around and is best avoided if a relative link is possible. The client will ask for the page  *http://ts-ug-dev.lifesci.dundee.ac.uk/BS32011/README.md*

The third link is a *fully qualified URI* which contains all the information the client needs to find the page so it will go directly there. This is the style you would use for referring to pages on external servers.

#### Internal links (anchors)

In a big web page it can be helpful to have internal anchors. These are specified with the form

   <a name="myanchor" />
   
(the /> at the end means we don't have to put in a separate </a> close tag.). This can then be accessed with the links

    <a href='#myanchor'>Internal link to My Anchor</a>
	<a href="mypage.html#myanchor">relative link from another page to my anchor</a>
	<a href=http://myserver/path/to/mypage.html#myanchor>Fully qualified link</a>

#### Exercise:
	
Create a second web page to describe your studies in this semester (eg. studies.html). Include a list at the top with internal links to each module. Add a link to this page from your home page.
	
### Images

There are several ways that images can be included in web pages. They can be used as the background for objects (which we will describe later when we look at CSS) or explicitly included using the *img* tag. 
The *img* tag takes several parameters - *src* describes the location of the image file to load and this can be a realtive, absolute or fully qualified URL. *width* and *height* specify the height and width  respectively.

There are several images in the *cgi* directory. you can either copy them (or an image of your own choosing) to your web folder or reference them with an absolute path (/BS32011/cgi/image1.jpg). Place code similar to the following in your web page:

    <img src='/BS32011/cgi/image1.jpg' />
	
This will probably be very big when you look at the page so adjust the height and width to suit.

    <img src='/BS32011/cgi/image1.jpg' height=120 width=80 alt='After the first bioinformatics practical' />
	
The alt attribute specifies the text that appears when you put a mouse over , or the image is not loaded. It is a good idea to use this attribute. Note that the text is between quotes. Either single or double quotes are fine.


### Tables

[reference: http://www.w3schools.com/html/html_tables.asp](http://www.w3schools.com/html/html_tables.asp)

Tables are block elements that contain rows, which contain cells.

	<table>
	    <tr>
		    <td> ... </td>
		</tr>
	</table>
	
The first row ( *tr* element ) can contain specific header elements ( *th* ) instead of the normal *td*. Tables are very flexible. You can nest tables (put the inner table in a *td* element of another) and put almost any other elements inside a table cell. Take a look at the linked table web page to discover how to set column widths, captions, cells spanning more than one column etc.

#### Exercise:
 
Rewrite your studies.html page to use tables instead of lists for your modules.
  
### Form elements

But what about form elements? That will follow shortly. First we'll look at making it all look nice with styles.

