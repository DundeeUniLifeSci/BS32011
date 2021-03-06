<h2>Testing functions</h2>
[reference: Assertions](https://wiki.python.org/moin/UsingAssertionsEffectively)
[reference: Exceptions](http://docs.python.org/2/tutorial/errors.html)
When writing code of any type, it's important to periodically check that your code does what you intend it to do. If you look back over the solutions to exercises from previous sessions, you can see that we generally test our code at each step by printing some output to the screen and checking that it looks OK. For example, in section 2 when we were first calculating AT content, we used a very short test sequence to verify that our code worked before running it on the real input.

The reason we used a test sequence was that, because it was so short, we could easily work out the answer by eye and compare it to the answer given by our code. This idea – running code on a test input and comparing the result to an answer <b>that we know to be correct</b> (Think of it as similar to running a positive control in a wet-lab experiment) – is such a useful one that Python has a built-in tool for expressing it: <code>assert</code>. An assertion consists of the word assert, followed by a call to our function, then <b>two</b> equals signs, then the result that we expect.

For example, we know that if we run our <code>get_at_content</code> function on the DNA sequence "ATGC" we should get an answer of 0.5. This assertion will test whether that's the case:


    assert get_at_content("ATGC") == 0.5


Notice the two equals signs – we'll learn the reason behind that in the next section. The way that assertion statements work is very simple; if an assertion turns out to be false (i.e. if Python executes our function on the input "ATGC" and the answer isn't 0.5) then the program will stop and we will get an <code>AssertionError</code>.

Assertions are useful in a number of ways. They provide a means for us to check whether our functions are working as intended and therefore help us track down errors in our programs. If we get some unexpected output from a program that uses a particular function, and the assertion tests for that function all pass, then we can be confident that the error doesn't lie in the function but in the code that calls it.

They also let us modify a function and check that we haven't introduced any errors. If we have a function that passes a series of assertion tests, and we make some changes to it, we can re-run the assertion tests and, assuming they all pass, be confident that we haven't broken the function (This idea is very similar to a process in software development called <i>regression testing</i>).

Assertions are also useful as a form of documentation. By including a collection of assertion tests alongside a function, we can show exactly what output is expected from a given input.

Finally, we can use assertions to test the behaviour of our function for unusual inputs. For example, what is the expected behaviour of <code>get_at_content</code> when given a DNA sequence that includes unknown bases (usually represented as <code>N</code>)? A sensible way to handle unknown bases would be to exclude them from the AT content calculation – in other words, the AT content for a given sequence shouldn't be affected by adding a bunch of unknown bases. We can write an assertion that expresses this:


    assert get_at_content("ATGCNNNNNNNNNN") == 0.5


This assertions fails for the current version of <code>get_at_content</code>. However, we can easily modify the function to remove all <code>N</code> characters before carrying out the calculation:

    def get_at_content(dna, sig_figs=2):
        dna = dna.replace('N', '')
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        return round(at_content, sig_figs)
        
and now the assertion passes.

It's common to group a collection of assertions for a particular function together to test for the correct behaviour on different types of input. Here's an example for <code>get_at_content</code> which shows a range of different types of behaviour:


    assert get_at_content("A") == 1
    assert get_at_content("G") == 0
    assert get_at_content("ATGC") == 0.5
    assert get_at_content("AGG") == 0.33
    assert get_at_content("AGG", 1) == 0.3
    assert get_at_content("AGG", 5) == 0.33333

A slightly more structured way to group tests is using Python's built-in testing framework. This involves writing a class definition - we won't go into details on how it works, but here's an example:

    import unittest
    
    def get_at_content():
        ...
    
    class TestATContent(unittest.TestCase):
    
        def test_single_base(self):
            self.assertEqual(get_at_content("A"), 1)
    
        def test_lowercase(self):
    		self.assertEqual(get_at_content("agtc"), 0.5)
    
    if __name__ == '__main__':
        unittest.main()

We can add as many testing functions as we like, and when we run the script on the command line it will run all the functions one after another and print out a report. This is a nice approach because we can give the testing functions meaningful names, so that when one of them fails it's obvious what the incorrect behaviour is. 
    
###Exercise

Look back at the code you've written for the exercises in the last session (writing functions). Write assertions to test each of the function calls that were specified in the exercise text, and verify that your answers pass the assertions. Can you think of any other tricky cases to test?


## Exceptions

Python has another way of handling errors which is to raise exceptions. These are useful in handling errors gracefully. It would be rather awkward if a program failed part way through an analysis where it had half completed and you had no way of tracking down the error.

Try the following in a python shell

    a = 5
	b = '6'
	c = 'seven'
	a+b
	int(a)+int(b)
	int(c)
	
We can see that some of these commands raise errors. Lets put this into a simple program that will calculate the average of numbers in a file, one per line. Save this as numbercount.py

    #!/usr/local/bin/python
    fh=open('numbers.txt') # open our data file
	total=0 # total of numbers read so far
	count=0 # count of numbers read so far
	for n in fh.readlines(): # iterate through the file one line at a time
		total=total+int(n) # we read in a string so int() converts to a number
		count=count+1
	fh.close()
	print "%s numbers read with a total of %s"%(count, total)
	
Now run the program

    python numbercount.py
	
Errors occur. The file of numbers has been badly written and will take ages to go through by hand and sort out. Maybe we can get the program to do this with exception handling?

Edit the program to the following:

    #!/usr/local/bin/python
    fh=open('numbers.txt') # open our data file
	total=0 # total of numbers read so far
	count=0 # count of numbers read so far
	skipped=0 # number of bad data points
	for n in fh.readlines(): # iterate through the file one line at a time
		try:
		    total=total+int(n) # we read in a string so int() converts to a number
		    count=count+1
		except:
		    print "Bad data %s - skipped"%n.rstrip() #take off the newline at the end of the string.
			skipped=skipped+1
	fh.close()
	print "%s numbers read with a total of %s. %s skipped."%(count, total, skipped)


We can get the message that python gives with the exception by using

    try:
		... code to test
	except Exception, e:
	    print 'the exception was %s'%e
	
The value of the exception is in the object e

We can handle different exceptions with different blocks

    try:
	    ... code to test
	except ValueError, ve:
	    ... handle value errors
	except AssertionError, ae:
	    ... handle assert errors
	except Exception, e:
	    ... catch any unhandled exceptions
		
And we can raise our own exceptions:

    raise Exception('Error message')
	
If you want specific errors then you can create your own by subclassing Exception

    class BadProgrammingError(Exception):
	    '''An Exception raised when a silly mistake has been made'''
		
and then use it as:
	
	raise BadProgrammingError('message') 
	
and

	try:
		... stuff
	except BadProgrammingError, bpe:
	    ... handle error
		
