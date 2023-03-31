# stunda
STUNDA = Sveriges Tekniska Universitets Nätverk för Datatermer

A dump of the data is stored in two formats,

- `stunda-terms.jsonl`
- `stunda-terms.tsv`

The part-of-speech (POS) information is in most cases guessed, marked `N?`

The file was created with the script described below.

## Directories

- `rawdata`: data copied from heterogeneous sources with no common format required. The starting point of the project.
- `scripts`: scripts analysing and converting rawdata

## Running the script

See instructions at the beginning of `scripts/convert_data.py`
