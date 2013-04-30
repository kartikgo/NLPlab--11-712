NLPlab--11-712
==============

This is a repository for the course 11-712. This project deals with building a morphological analyzer for the Spanish language.

[Results-> Spanishfinal.bin] is the binary file for the analyzer.

How to use the analyzer:
cat <input_file> | flookup <path-to-analyzer>/Spanishfinal.bin

For modification: The file lex.foma is the foma file which can be modified.
All the lexc files mentioned in the foma file are available for modification in the src folder.
TO DO:
Quantitative analysis on Corpus-B.
