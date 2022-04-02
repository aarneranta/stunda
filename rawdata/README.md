# raw data files

## ACM-klassificering-1998-en-sv.xls	


## ICT-keywords-20141203.xlsx

The columns in the spreadsheet are "English - Word or Words", "Swedish", "URL to definition or usage".

The list of English words were mechanically extracted from the IK2554 lecture notes in June 2014. The initial translation was done by G. Q. Maguire Jr. with the assistance of Google Translate; Nordstedts Stora Engelska Ordbook, Tredje Upplag, 2000; Computer Sweden Ordlistan;   and Svenska Datatermgruppen. MH checked and corrected the Swedish terms in August 2014. I (GQMJr) am particularly thankful for his addressing the problem of when the same word in English is used as both a noun and verb, while in Swedish two different words are used. In the next step the keywords using in ICT theses 2010-2014 were added to the list along with the Swedish translations when there was a paired translation available. These were then manually edited.

In November-Decomber 2014 GQMJR added the worlds extracted from the slides and lecture notes for IK2555. Acronyms, brandnames, personal names, ... were manually removed.
Notes: 

A vertical bar ("|")  indicates the same root with and without the letter(s) following the vertical bar exists. Generally this indicates plurals of nouns, but in some cases concerns a noun and verb. For example: "acceleration|s", "acceleration|er".

A "/" indicates either alternatives (in an expression such as "and/or") or alternatives words. This is common in the Swedish column to separate a noun and verb (when the same word in English translates to a different noun and verb in Swedish).


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



