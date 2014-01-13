# Getting data from the user with web forms - the web page side.

The primary way that web pages interact with servers to send them specific information is though web forms. These 
capture information from the user and transfer it to the server.

Forms contain a specific set of elements which, when submitted, take their contents and transfer them to the server as 
part of the query.

### Form structure

Forms contain a *form* element which will then contain one or more *input* elements, or other elements that can take input
(such as a *textarea* text box or a *select* drop-down list.) With a small bit of Javascript it is possible to coerce 
almost anything into providing input for a form but we are not going to cover that in this course.

Here is a document fragment containing a simple form:

    <form id=myform name=myform method=POST action=formprocess.py>
    	<input type=text size=20 name=title value='Write a title'/>
    	<textarea rows=5 col=40 name=description>Write a description here</textarea>
    	<input type=submit name=submit value='Do something' />
    </form>



#### The form element

[reference: http://www.w3.org/community/webed/wiki/HTML/Elements/form](http://www.w3.org/community/webed/wiki/HTML/Elements/form)

The most important attributes of the form element are:

* action - this is the URL to which the form inforomation is sent for processing
* method - specifies the request method (GET or POST)
* name - the name of the form
* enctype - The encoding used. Important for doing file uploads.

In addition you can use the usual *class=*,  *id=*, *style=* etc. attributes.

The *form* element can contain normal layout elements to allow it to be nicely formatted, typically a *table*. 
Here is the form from earlier placed in a table:

    <form id=myform name=myform method=POST action=formprocess.py>
    	<table>
	    	<tr><td>Title:</td>
		    <td><input type=text size=20 name=title value='Write a title'/></td></tr>
		    <tr><td>Description</td>
	    	<td><textarea rows=5 col=40 name=description>Write a description here</textarea></td></tr>
	    	<tr><td></td><td><input type=submit name=submit value='Do something' /></td></tr>
    	</table>
    </form>

#### Input elements

[reference: http://www.w3.org/community/webed/wiki/HTML/Elements/input](http://www.w3.org/community/webed/wiki/HTML/Elements/input)

The *input* element can be represented in a variety of types. These take different attributes. The most common are:

* [text](http://www.w3.org/community/webed/wiki/HTML/Elements/input/text) - takes a plain text value from the user.
* [hidden](http://www.w3.org/community/webed/wiki/HTML/Elements/input/hidden) - encodes a value but the user doesn't see it and cannot edit it.
* [submit](http://www.w3.org/community/webed/wiki/HTML/Elements/input/submit) - creates a submission button
* [checkbox](http://www.w3.org/community/webed/wiki/HTML/Elements/input/checkbox) - creates a tickbox 

There are many other input types - they will validate the data is of the correct form (ie an email address field is a text field which takes data that looks like a valid email). Some may open specific *widgets* (ie a calendar selection).

Each of these input fields should have a unique name in that form. This name is used to identify that bit of data when it is submitted to the server which will process it.

#### Textarea elements
[reference: http://www.w3.org/community/webed/wiki/HTML/Elements/textarea](http://www.w3.org/community/webed/wiki/HTML/Elements/textarea)

The *textarea* element is intended for a larger, typically multiline, block of text. As well as the essential *name* attribute, it has *rows* and *cols* for specifying the size of the box on the screen.

#### Drop-down lists

[reference: http://www.w3.org/community/webed/wiki/HTML/Elements/select](http://www.w3.org/community/webed/wiki/HTML/Elements/select)

The *select* element provides a multiple choice list from a set of options. Key parameters are:

* name - essential for the element.
* multiple - If set it allows the user to specify more than one option
* size - shows that number of options. If multiple is set then it shows a scrollable list. If multiple is not set then a drop down list is shown.

Each *select* element contains a number of option elements. The *option* elements have a value attribute which dictates the values passed by the form.

    <select name=myselect >
        <option value=1>First option</option>
        <option value=2>Second option</option>
    </select>

This element contains two values which are displayed ysing the text in the *option* tag but the value the form sends is set by the value attribute. If value is not set then the text between the *option* tags is used as the value.

 
#### Exercise:

Write a web page containing a form for restriction enzyme digestion of a sequence. Your form should contain fields for:

* the sequence name
* the sequence
* a choice of restriction enzyme from the four below.

Don't forget a submit button! You will use a *select* element for the restriction enzyme choice. Use the enzyme name as the value and a description of it's cut site as the display text.

    EcoRI     G^AATTC
    SmaI      GGG^CCC
    HindIII   A^AGCTT
    PstI      CTGCA^G





