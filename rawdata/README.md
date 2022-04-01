# raw data files

## ACM-klassificering-1998-en-sv.xls	


## ICT-keywords-20141203.xlsx


## gf-termsEngSwe.tsv

Terms collected by a bachelor project group at Chalmers in 2020.
Original source: https://github.com/translator-for-cs/translator-for-cs

Columns in the tsv file:
```
abstract syntax tree | English word forms | Swedish word forms
```
The abstract syntax tree indicates a classification by parts of speech:

- N: noun
- CN: (possibly complex) noun
- AP: adjective
- V: verb
- Adv: adverbial

The data was dumped from the files grammars/Yerms*.gf with GF commands,
```
> i TermsSwe.gf TermsEng.gf
> gt -cat=NCSE | l -tabtreebank -list | wf -file="gf-termsEngSwe.tsv"
```
and so on for the other four categories.

The main source of the data was Chalmers CSE course plans. Morphology is derived from SALDO and GF's morphological functions, and has not been completely verified. Translations have not been completely verified either.



