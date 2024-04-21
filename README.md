# UR to SR mapping over 13 parameters
This project creates mappings of every licit combination of (meaninglessly ordered) underlying lexical items (n=8) to a resultant Surface Order of Words (SOWs/SRs/"a sentence").  Each "sentence" mapping is produced by feeding an Underlying Representation (UR/abstract form of an utterance) into a static syntactic tree and then applying the rules of a particular parameter set (features of a "language family").  In the syntactic tree, each lexical item has a fixed birthplace, prescribed movement loci, and is underlyingly null until it is turned on (through explicit presence in the UR or a parameter setting being on or off, etc.).

This mapping project is intended to be used by an Expectation Maximization learning algorithm (Expectation Driven Learning (EDL)) as input data.  Working through each UR-to-SR mapping in a language family's data, such an algorithm updates its beliefs about what language is being viewed.  This algorithm is essentially a proxy for human language learning under the principles and parameters model, in which the marginal addition of language data from each utterance updates a learner's assumptions about the language family they are learning, and the grammatical attributes of their language family.

Thus, this project represents an abstracted sample of language data that a human learner would encounter while learning a language, with the UR representing something like the semantically meaningful items and the SR/SOW representing the heard or produced utterance.

The parameters of the current project are based on the 13 outlined in a [Sakas & Fodor 2012 article](http://www.colag.cs.hunter.cuny.edu/pub/Sakas_Fodor_Disambiguating_prepub.pdf#24).  We analyzed the structure of their parametric grammar in order to produce a mapping that would be more appropriate for feeding to the EDL algorithm.

The language family set created by the 13 parameters and resulting in 8192 "language families" are extendable/scalable by adding additional parameters in [src/parameters.py](https://github.com/rofgh/ur_to_sr_mapping/blob/04ee506608f7c58b81418987d333ec76d639e712/src/parameters.py#L1).  Depending on the format of this parameter, this will require the addition of syntactic tree lexical item(s), which would need to be reflected in [nodes.py](https://github.com/rofgh/ur_to_sr_mapping/blob/04ee506608f7c58b81418987d333ec76d639e712/src/nodes.py#L1) and changes to the [UR_writer](https://github.com/rofgh/Hidden-Sin/tree/master/UR_writer).  Essentially, scaling by another parameter requires some fluency in the script, but is reasonably possible.

See the [src readme](https://github.com/rofgh/ur_to_sr_mapping/blob/master/src/README.md) for more in depth descriptions of the code.

Our preliminary thoughts/description/notes/analysis/interpretation of the original SFY grammar and languages can be found [here](https://docs.google.com/document/d/1J_fS85IQWB9MPXB96ccHrKF_JHXn44iVyyemQOeFJQo/edit?usp=sharing)

## parent.py
This is the script to run on the command line (python3).  (There is a [Makefile](https://github.com/rofgh/ur_to_sr_mapping/blob/04ee506608f7c58b81418987d333ec76d639e712/Makefile#L1))  
This file takes four arguments, default=False/None in order to run a smaller domain, and begins the ur_to_sr_mapping code set.   ("python parent.py" = "python parent.py False False False run" )

`make full` or `python parent.py True True True all_all`, which will run all 8192 language families (2GB worth of tsv files) (~8 hour run time)

`make run` or `python3 parent.py False False False run` which will run a small subset of user-modified variables (see Arguments, below)

#### Arguments  
1  (True OR False) (Default = False)  
The first boolean argument determines whether all 13 parameter language families are run (True) (n=8192) or whether only the [limited, user-modified list](https://github.com/rofgh/ur_to_sr_mapping/blob/1ab96bdabc231e07334c53806e0bcb91129e5752/src/ind_variables.py#L16) is assessed (False).

2  (True OR False) (Default = False)  
The second boolean argument determines whether all forces are assessed (True) (n=3) or whether only the [limited, user-modified list](https://github.com/rofgh/ur_to_sr_mapping/blob/1ab96bdabc231e07334c53806e0bcb91129e5752/src/ind_variables.py#L5) is assessed (False).

3  (True OR False) (Default = False)  
All possible UR permutations are assessed (True) (n=???) or the [limited, user-modified list](https://github.com/rofgh/ur_to_sr_mapping/blob/1ab96bdabc231e07334c53806e0bcb91129e5752/src/ind_variables.py#L47)) (False).

4  (folder name) (default = "run")
Argument 4 is an output folder name into which to create the output files. Avoid "all_all", unless re-making the master list of all permutations (`parent.py True True True all_all`).  Otherwise the script will overwrite the entire library of mappings (and thus overwrite 8 hours of work).
***

### ind_variables.py  
Contains all the limited lists of forces, language families, URs to map if the respective False arguments are given to parent.py; and the list of licit SRs to test against the output SRs after the mapping is complete.

### various.py  
This script contains a range of smaller functions, which don't seem to have a better place to be brought together

### timeme.py  
Contains the various timing functions, including how often to change to a new filename (allowed_per_file())

### URs.py  
Produces all needed URs, defaulting to all three illocutionary forces

### test_parse.py  
Ensures that known licit SR parses, cataloged in ind_variables.py, are produced by the parent.py UR-->SR script.  (Currently does not pass if the parent script is only given a limited UR list, as the test cases include many of the possible lexical items.)

## Results Examples
The last time the code was fully run it took 7 hours 39 minutes.  One change, that I am hoping helps this speed is to split the tsv files, so that a large fil isn't being opened to be appended to, though I haven't run the full mapping since implementing these changes.  Since the data file starts out at 0MB and by the end of the run it is 2GB, it starts being taxing to open the file in order to write to it (I presume?).  ![Code Complete](ScreenshotAllFinished.png)

### 10/14/21
Update after running with the files being split every ten minutes, instead of using just one tsv file:  
Entire run took 6 hours 47 minutes, so maybe splitting the tsv files helped reduce the time a bit, but only by 11%.  So, maybe I should scrutinize how the script is writing to the tsv files, as having it do so for every line is probably a waste of time and it should be, for example, storing all the mappings for a language family, then dumping these to the tsv file once all the mappings for that language family are complete, etc.
![Code Complete 10/14/21](ScreenshotAllFinished21.png)

A sample from all_all.tsv looks like:
```bash
0000000000100	D	S	Verb            SR:	Not parseable because of Parameter: 4: no topic and topic is obligatory			
0000000000100	D	S	Verb	Aux     SR:	Not parseable because of Parameter: 4: no topic and topic is obligatory			
0000000000100	D	S	Verb	Adv	    SR:	Not parseable because of Parameter: 4: no topic and topic is obligatory			
0000000000100	D	S	Verb	O1		SR:	Not parseable because of Parameter: 4: no topic and topic is obligatory
0001001100011	D	S	Verb            SR:	S	Verb
0001001100011	D	S	Verb	Aux		SR:	S	Aux	Verb
0001001100011	D	S	Verb	Adv	    SR:	S	Verb	Adv
0001001100011	D	S	Verb	O1		SR:	S	Verb	O1
0001001100011	D	S	Verb	PP		SR:	S	Verb	P	O3
0001001100011	D	S	Verb	Aux	Adv	SR:	S	Aux	Verb	Adv
0001001100011	D	S	Verb	Aux	O1	SR:	S	Aux	Verb	O1
0001001100011	D	S	Verb	Aux	PP	SR:	S	Aux	Verb	P	O3	
```
For the first example language family (0000000000100), none of the sentences are parseable.  If the UR were parseable, the licit SR(s) would be provided, as with the second language family (0001001100011), where the SRs are shown following the URs.

With this structure, a learning algorithm would pull the UR-SR mappings from the all_all.tsv files by separating the language, force, UR and SR on each line.

### Github Folders:  
[src](https://github.com/rofgh/ur_to_sr_mapping/tree/master/src): these are the modules accessed by parent.py and sr_creator.py.  Also contains [UR_writer](https://github.com/rofgh/Hidden-Sin/tree/master/src/UR_writer):  Scripts that create the URs

[grabber](https://github.com/rofgh/ur_to_sr_mapping/tree/master/grabber): this script pulls the SRs (and, optionally, the URs) form the original CoLAG data.  It is used for confirming correct production of this project.  

[S_F_Y_Data_Files](https://github.com/rofgh/ur_to_sr_mapping/tree/master/S_F_Y_Data_Files)  

[Misc](https://github.com/rofgh/Hidden-Sin/tree/master/Misc): Items that got put into the Notes shared doc, etc.  

[EDL Learner](https://github.com/rofgh/Hidden-Sin/tree/master/EDL%20Learner): Original 6 parameter script, etc.  

[Reference Papers](https://github.com/rofgh/ur_to_sr_mapping/tree/master/Reference%20Papers)   
 



