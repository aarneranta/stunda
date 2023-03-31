import pandas
import json
import sys

"""
Convert different data sources to a common TSV or JSON format.

Usage:

  python3 convert_data TSV

reads the sources from ../rawdata and writes to stunda_terms.tsv

  python3 convert_data JSON

reads the generated TSV file and writes ../stunda-terms.json
containing a JSON list of dictionaries, one per term

  python3 convert_data JSONL

reads the generated TSV file and writes ../stunda-terms.jsonl
containing one dictionary per lien, for each term.
"""

TSV_INPUT_FILE = '../stunda-terms.tsv'
JSON_OUTPUT_FILE = '../stunda-terms.json'
JSONL_OUTPUT_FILE = '../stunda-terms.jsonl'


MODE = 'TSV'
if sys.argv[1:]:
    MODE = sys.argv[1]


delimiter = '\t'  # generate tsv

rawdata_path = '../rawdata/'

data_files = [
    {'name': 'ACM-klassificering-1998-en-sv.xls', 'cols': [3, 4], 'add': [('N?', 2), ('0', 3)], 'format': 'excel', 'abbr': 'ACM'},
    {'name': 'ICT-keywords-20141203.xlsx', 'cols': [0, 1],  'add': [('N?', 2), ('0', 3)], 'format': 'excel', 'abbr': 'ICT'},
    {'name': 'shorter-gf-termsEngSwe.tsv', 'cols': [0, 1, 2], 'add': [('1', 3)], 'format': 'tsv', 'abbr': 'GF'},
    ]

def data2csv(filedata):
    if filedata['format'] == 'excel':
        pds = pandas.read_excel(rawdata_path + filedata['name'], dtype=str, usecols=filedata['cols'])
    elif filedata['format'] == 'tsv':
        pds = pandas.read_csv(rawdata_path + filedata['name'], sep='\t', usecols=filedata['cols'])
    return pandas.DataFrame.to_csv(pds, sep=delimiter).split('\n')


def uncap(s):
    s = s.strip()
    if False and s and not s.isupper():
        return s[0].lower() + s[1:]
    else:
        return s
    

def convert_all():
    lines = []
    for file in data_files:
            for line in data2csv(file):
                fields = line.split('\t')
                if fields[1:]:
                    fields[0] = uncap(fields[0]) 
                    fields[1] = uncap(fields[1]) 
                fields.append(file['abbr'])
                fields.append(fields[0])
                fields = fields[1:]
                for field, pos in file['add']:
                    fields.insert(pos, field)
                lines.append('\t'.join(fields))
    lines.sort(key = lambda line: line.lower())
    header = '\t'.join(['English', 'Swedish', 'POS', 'source', 'row'])
    lines.insert(0, header)
    with open(TSV_INPUT_FILE, 'w') as outfile:
        outfile.write('\n'.join(lines))


def get_forms(xs):
    if xs:
        return {'lemma': xs[0], 'inflection': xs[1:]}
    else:
        return None
    

def to_json():
    with open(TSV_INPUT_FILE, 'r') as infile:
        terms = []
        if MODE == 'JSONL':
            jsonfile = JSONL_OUTPUT_FILE
        else:
            jsonfile = JSON_OUTPUT_FILE
        with open(jsonfile, 'w') as outfile:
            for line in infile:
                fields = line.split('\t')
                if len(fields) > 5:
                    dict = {
                        'eng': get_forms(fields[0].split(', ')),
                        'swe': get_forms(fields[1].split(', ')),
                        'pos': fields[2],
                        'status': fields[3],                      # 0 = unchecked, 1 = checked
                        'src': fields[4],
                        'row': fields[5].strip(),
                        'comment': 'from data',
                        'synonyms': [],
                        'definition': None
                        }
                    if MODE == 'JSONL':
                        outfile.write(json.dumps(dict, ensure_ascii=False)+'\n')
                    else:
                        terms.append(dict)
            if MODE == 'JSON':
                json.dump(terms, outfile, ensure_ascii=False, indent=2)
        
if __name__ == '__main__':
    if MODE == 'TSV':
        convert_all()  # initial conversion from data: save in TSV_INPUT_FILE, which is easier to edit
    else:
        to_json()


