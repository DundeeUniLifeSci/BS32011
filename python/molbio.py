'''Collection of classes to represent objects useful in Molecular Biology'''


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