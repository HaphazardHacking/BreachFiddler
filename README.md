# BreachFiddler

Simple python scripts for organising and searching through files from breaches.

Current progress / TODO:

- decomp.py, takes directory path as an argument, recursively extracts all files from .tar.gz archives, deletes archives when done.
- collate.py, takes directory path as an argument, recursively collates all files into 1GB files in directory called _collation_output
- dedup.py, takes directory path as an argument, deduplicates lines within each file, *needs to be re-done once sorting by domain is done*
- domainsort.py, re-done, much quicker.
- search.py, TODO
-
- code comments, very much TODO
- multi-threading, domainsort is pretty good but could be quicker
