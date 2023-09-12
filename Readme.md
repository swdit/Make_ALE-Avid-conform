# Make ALE Avid-conform



> No operational version yet available - Project in early stage


This Python-Script will check an ALE file (AvidLogExchange) for known issues that might cause problems when imported into Avid-Media-Composer (AMC) and fix them:
This is primarily targeted to ALE's that have been generated in third party tools (Silverstack, DaVinci-Resolve...) and not by Avid-Software.

### Issues this Script would fix in an ALE:
1. Character limit:
Plenty versions of AMC will crash if an ALE with more than 250 characters, in one Metadata field, is imported.
This script will find those fields, cut them down to 247 characters, and attach the suffix "..."; to give a hint that data had to be cut off.


2. German-Umlaut
Plenty Version of AMC struggle with special german characters like "ö, ä, ü, ß".
This script will address the German umlauts by writing them out without any special characters.

> Common ALE-Issue missing?
> 
> Feel free to get in touch via github to request further ALE-conforming  
> https://github.com/swdit/Make_ALE-Avid-conform/issues


### Installation

1. Install Python 3.10 (other versions might work as well but have not been tested) 
- https://www.python.org/downloads/

2. Install dependencies
- Pandas `pip install pandas`

### Usage

1. Execute script `python3 Make_ALE-Avid-conform.py`
2. Filedialog will open select ALE to be checked
3. Script will place three new files in the source directory
    1. fixed dataset as ALE
   2. fixed dataset as identical CSV (easier to be opened in tools like numbers, calc, excel for manual check)
   3. log-file listing the changes


### Upcoming features

#### Watchfolder

script would automatically be executed on new ALE's appearing in a specific folder


#### Skip if already conform

script will not generate new ALE and CSV if no changes are necessary

#### Configuration YAML

Set up a configuration YAML allowing for some customisation
- skip CSV creation
- specify rows to be deleted
-  specify sets of additional characters or formulations to be replaced




 
 