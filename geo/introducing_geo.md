# Exploring the Gene Expression Omnibus

[GEO can be found at NCBI](http://www.ncbi.hih.gov/geo). Each of the studies represented has an identifier that starts with GDS (ie GDS3001). The data files can be found at the [FTP site](ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/) where you navigate to the dataset you wish to download.

The datasets are available in two versions - an abbreviated version with just the values and a gene identifier, and a full version - we'll look at these below. Download the appropriate dataset and uncompress it with 

    gunzip dataset.gz
    
(obviously changing dataset.gz to the name of the file you have downloaded). I'm using GDS3001 as an example.

### Data file format
Take a look at your data file with 

    more datafile
    
The top of the file is the header which contains details of the experiment. Each header line starts with '^', '!' or '#'. The lines beginning with '^' denote a section in the header. For example the first section is 
    ^DATABASE = Geo
which states the database source. This is followed by various fields describing GEO

The second section describes the complete datase.
    ^DATASET = GDS3001
Key things to note in this section are the fields 
    !dataset_type = Expression profiling by array
    !dataset_channel_count = 1
    !dataset_sample_count =1
    
This is a single channel experiment so we don't have to worry about dye swaps, and there are 14 samples in the study.

The samples are divided into subsets for the replicates of each sample type.

    ^SUBSET = GDS3001_1
    !subset_dataset_id = GDS3001
    !subset_description = vehicle control
    !subset_sample_id = GSM185015,GSM185016,GSM185017,GSM185018,GSM185019
    !subset_type = protocol

And we can see a list of sample ID's that form this subset. These sample IDs are the column headers in the data table.

    ^Annotation

describes how the dataset has been annotated. Our knowledge of gene function changes over time so it is important to understand what the state of knowledge was at the time the conclusions were drawn.

    ^DATASET = GDS3001
appears a second time. The subsequent rows describe the columns in the data table. Each row starts with '#' and gives the column name and a description.
    #ID_REF = Platform reference identifier
    #IDENTIFIER = identifier
    #GSM185015 = Value for GSM185015: DIO Vehicle 1; src: Vehicle treated liver from C57BL/6J DIO mice.
give the first three rows.
 
#### The data table

The bulk of the data is present as a table, the header of which starts with ID_REF and IDENTIFIER. This is followed by a number of columns corresponding to each individual set of values (ie each experiment in the study), and then by more columns ('Gene title' and so on) that describe the target of each probe in more detail. These are the column names defined in the header.

Here is the first few lines of the data table - each field is separated from teh next by a tab character ('\t').

    ID_REF  IDENTIFIER      GSM185015       GSM185016       GSM185017       GSM185018       GSM185019       GSM185020       GSM185021       GSM185022       GSM185023       GSM185024       GSM185025       GSM185026       GSM185027       GSM185028       Gene title      Gene symbol     Gene ID UniGene title   UniGene symbol  UniGene ID      Nucleotide Title        GI      GenBank Accession       Platform_CLONEID        Platform_ORF    Platform_SPOTID Chromosome location     Chromosome annotation   GO:Function     GO:Process      GO:Component    GO:Function ID  GO:Process ID   GO:Component ID
    1415670_at      Copg1   231.227 207.124 235.396 232.997 203.818 241.283 267.197 285.437 246.115 213.3   212.593 199.303 189.06  192.716 coatomer protein complex, subunit gamma 1       Copg1   54161                           Mus musculus coatomer protein complex, subunit gamma, mRNA (cDNA clone MGC:30335 IMAGE:3992144), complete cds   19354080        BC024686                                6 39.13 cM      Chromosome 6, NC_000072.6 (87887940..87913595)  structural molecule activity    establishment of Golgi localization///intracellular protein transport///organelle transport along microtubule///protein transport///transport///vesicle-mediated transport      COPI vesicle coat///Golgi apparatus///Golgi membrane///cytoplasm///cytoplasmic vesicle///membrane///membrane coat///nucleus     GO:0005198      GO:0051683///GO:0006886///GO:0072384///GO:0015031///GO:0006810///GO:0016192     GO:0030126///GO:0005794///GO:0000139///GO:0005737///GO:0031410///GO:0016020///GO:0030117///GO:0005634
    1415671_at      Atp6v0d1        492.646 443.456 483.607 460.328 444.518 489.331 421.409 445.804 390     505.714 427.916 492.811 452.398 455.307 ATPase, H+ transporting, lysosomal V0 subunit D1        Atp6v0d1        11972                           Mus musculus ATPase, H+ transporting, lysosomal V0 subunit D1 (Atp6v0d1), mRNA  141802838       NM_013477                               8       Chromosome 8, NC_000074.6 (105524470..105566040, complement)    hydrogen ion transmembrane transporter activity///hydrogen-exporting ATPase activity, phosphorylative mechanism///protein complex binding       ATP catabolic process///ATP hydrolysis coupled proton transport///ion transmembrane transport///ion transport///proton transport///transport    apical plasma membrane///axon terminus///colocalizes_with centrosome///early endosome///membrane///neuron projection///protein complex///proton-transporting V-type ATPase, V0 domain///synaptic vesicle///vacuolar proton-transporting V-type ATPase complex   GO:0015078///GO:0008553///GO:0032403    GO:0006200///GO:0015991///GO:0034220///GO:0006811///GO:0015992///GO:0006810     GO:0016324///GO:0043679///colocalizes_with GO:0005813///GO:0005769///GO:0016020///GO:0043005///GO:0043234///GO:0033179///GO:0008021///GO:0016471
The end of the table is marked by the line

    !dataset_table_end
    
### Representing your datafile in SQL

Think about how you want to represent your data. Which fields can be foreign keys referring to other tables? How many and which tables do you need? Do you need to represent all the data? It might be best to start off with representing the minimal amount you can and then work up form there if you are feeling bold/have time.

You will then need to read the data in from the file - how will you parse it into values and insert it into the database?

When you have thought about this, discuss your plans with Dr Martin.


