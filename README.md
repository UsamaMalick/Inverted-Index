# Inverted-Index
Inverted Index of english language files

This INVERTED INDEX is divided in three tasks and each task is expalained below.

# Task 1: Tokenizing Documents

The first step in creating an index is tokenization. Document is converted into a stream of tokens suitable for indexing.
#### Tokenizer follow these steps:
Accept a directory name as a command line argument, and process all files found in that directory.

􏰤Extract the document text and split the text into tokens.

􏰤Convert all tokens to lowercase (this is not always ideal, but indexing intelligently in a case-sensitive manner is tricky) Also need to remove punctuation and numbers.

􏰤Prepare a list of stop words from the dataset, and apply stopping. 
(This will require some intelligent decision as to how many stop words you should remove).

􏰤Apply stemming to the document using any standard algorithm 􏰧 Porter, Snowball, and KStem stemmers are appropriate.

### 􏰤Tokenizer will write two files:
##### 1 - docids.txt 􏰧 
A file mapping a document's filename to a unique integer, its DOCID. Each line is formatted with a DOCID and filename separated by a tab, as follows:
1234\t324352 

##### 2 - term_ids.txt 
A file mapping a token found during tokenization to a unique integer, its TERMID. Each line is formatted with a TERMID and token separated by a tab, as follows:
567\tapple

