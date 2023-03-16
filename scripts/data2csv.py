import pandas
import json
import sys

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
    if s and not s.isupper():
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
    print('\t'.join(['English', 'Swedish', 'POS', 'source', 'row']))
    for line in lines:
        print(line)


def get_forms(xs):
    if xs:
        return {'lemma': xs[0], 'inflection': xs[1:]}
    else:
        return None
    

TSV_INPUT_FILE = '../all-terms.tsv'
JSON_OUTPUT_FILE = '../stunda-terms.json'

def to_json():
    with open(TSV_INPUT_FILE, 'r') as infile:
        terms = []
        with open(JSON_OUTPUT_FILE, 'w') as outfile:
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
                        'comment': 'from data'
                        }
                    if MODE == 'DICTS':
                        outfile.write(json.dumps(dict, ensure_ascii=False)+'\n')
                    else:
                        terms.append(dict)
            if MODE == 'JSON':
                json.dump(outfile, dict, ensure_ascii=False, indent=2)
        
if __name__ == '__main__':
    if MODE == 'TSV':
        convert_all()  # initial conversion from data: save in TSV_INPUT_FILE, which is easier to edit
    else:
        to_json()


