# Introducing python classes

### What is a _class_ ?

A class is a definition of an object. An object can contain both data and methods for manipulating that data. This allows a functional unit, or model of some concept to be _encapsulated_. 

Let's start with a simple object.

    class Gene():
	    '''This is a class that represents a gene.'''
	    sequence=''
	    accession=''
	
	    def __init__(self, accession, sequence):
		    '''Object initialiser. This takes two arguments, accession 
		    (the accession number) and the sequence. The sequence is 
		    stripped of newlines and converted to upper case.'''
		    self.sequence=sequence.upper().replace("\n","")
		    self.accession=accession.upper()
		
	    def setsequence(self, seq):
		    '''Sets the sequence to the string given, stripping newlines and converting to upper case'''
		    self.sequence=seq.upper().replace("\n","")
		
	    def getAT(self):
		    '''returns the AT count for the sequence'''
		    at_count=self.sequence.count("A")+self.sequence.count("T")
		    return at_count
	
	    def length(self):
		    '''Returns the length of the sequence.'''
		    return len(self.sequence)
		
We can now use this object in out code

    a=Gene("ABC123","acgtagctatcgcgatcggtatatttcgctatcgaggctaggctaggctagcttatatagctaggctagt")
	a.sequence
	a.accession
	a.getAT()
	a.length()

That is great. Now let's try cloning the gene (copying the object).
	
	b=a
	#make a copy of the gene
	b.accession="BCD234"
	b.accession
	a.accession
	
That's strange, why has the accession in *a* changed?
	
	# we haven't copied the gene, we have copied the reference to the object
	a
	b
	# these point to the same memory location.
	a=Gene("ABC123","acgtagctatcgcgatcggtatatttcgctatcgaggctaggctaggctagcttatatagctaggctagt")
	a 
	b
	#now they are different objects
	a.accession
	b.accession
	b.accession="CDE345"
	a.accession
	
We could add a clone() method that would allow us to copy genes easily

	class Gene():
	... other methods ...
        def clone(self):
		    '''Returns a copy of the gene.'''
		    return Gene(self.accession, self.sequence)

and then instead of copying it as b=a we do

    b=a.clone()
	
#### Exercise

    1 Add a description field to the class to hold a text description of the sequence. This should be stored as a one line string - convert any newlines to ; to join them into a single string.
    2 Add a method fasta() that will return a string containing the gene in FASTA format. For extra readability limit the number of bases in one line to 50, wrapping on to new lines as necessary.

    FASTA format:
    >ACCESSION Description all on one line
	SEQUENCE
	MORE SEQUENCE
	EVEN MORE SEQUENCE IF REQUIRED
	
	
	
### Superclasses, subclasses and heredity

It can be tiresome copying and pasting many lines of code to make small changes to an object definitition. Instead, where we have many similar objects we can use subclassing.

	class GeneFeature():
		'''represents an arbitrary gene feature'''
		gene=None
		start=None
		end=None
		orient=None
		type='Generic'
		notes={}
		
		def __init__(self, gene, start, end, **kwargs):
			'''Initialise with the gene, start, end and any notes desired. Position numbering starts at 1, not 0'''
			self.gene=gene
			self.start=int(start)
			self.end=int(end)
			for k in kwargs.keys():
			    self.notes[k]=kwargs[k]
			if self.start < self.end:
				self.orient='+'
			else:
				self.orient='-'
				
		def getNote(self, key):
			return self.notes.get(key,'')
			
			
	class CDS(GeneFeature):
	    code={ 'ATA':'I',
        'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T',
        'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S',
        'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L',
        'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
        'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R',
        'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A',
        'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E',
        'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S',
        'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
        'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 'TGC':'C',
        'TGT':'C', 'TGA':'*', 'TGG':'W'}
		
		def translate(self):
            '''translate the feature to an amino acid sequence. presumes forward orientation'''
			aa=''
			nt=self.gene.sequence[start-1:end]
			cod=0
			while cod<len(nt):
				aa=aa+self.code[nt[cod:cod+3]]
				#read the codon and get the corresponding amino acid to add to the aa sequence
				cod=cod+3
				#move on one codon
			return aa
			
CDS _inherits_ all the data and methods of GeneFeature and extends them. It adds a genetic code, and a 'translate' method.
				
Instead of writing this out every time we can save it in a file. Let's call it molbio.py

We can reuse this in any script now. Exit python (CTRL-D) and start it again.

    import molbio
	
	a=molbio.Gene()
	seq=molbio.CDS(a, 4, 20)
	seq.translate()
	
#### Exercise:
    Create a subclass of GeneFeature that encodes a restriction enzyme digest site. It should have a method cleave() which returns a list of two Gene objects corresponding to the two forward sequences resulting from cleavage.
	
