# stunda
STUNDA = Sveriges Tekniska Universitets Nätverk för Datatermer

Directories

- rawdata: data copied from heterogeneous sources with no common format required. The starting point of the project.
- scripts: scripts analysing and converting rawdata

Example: to get a sorted synopsis of all data, do
```
cd scripts
python3 data2cvs.py
```
This will write the synopsis in tsv form to standard output.

TODO:
- The list of raw data files is now hardcoded in data2cvs.py.
- Data in different files should be massaged further for more accurate
comparisons.

