# stunda
STUNDA = Sveriges Tekniska Universitets Nätverk för Datatermer

NEW 2023-02-24: a dump of all data in one table:

- all-terms.tsv

The part-of-speech (POS) information is in most cases guessed, marked `N?`

The file was created with the script described below.

## Directories

- rawdata: data copied from heterogeneous sources with no common format required. The starting point of the project.
- scripts: scripts analysing and converting rawdata

## Running the script

To get a sorted synopsis of all data, do
```
cd scripts
python3 data2cvs.py
```
This will write the synopsis in tsv form to standard output.

TODO:
- The list of raw data files is now hardcoded in data2cvs.py.
- Data in different files should be massaged further for more accurate
comparisons.

