import pandas
import json

delimiter = '\t'  # generate tsv

rawdata_path = '../rawdata/'

data_files = [
    {'name': 'ACM-klassificering-1998-en-sv.xls', 'cols': [3, 4], 'add': [('N?', 2)], 'format': 'excel'},
    {'name': 'ICT-keywords-20141203.xlsx', 'cols': [0, 1],  'add': [('N?', 2)], 'format': 'excel'},
    {'name': 'shorter-gf-termsEngSwe.tsv', 'cols': [0, 1, 2], 'add': [], 'format': 'tsv'},
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
                fields.append(file['name'])
                fields.append(fields[0])
                fields = fields[1:]
                for field, pos in file['add']:
                    fields.insert(pos, field)
                lines.append('\t'.join(fields))
    lines.sort(key = lambda line: line.lower())
    print('\t'.join(['English', 'Swedish', 'POS', 'source', 'row']))
    for line in lines:
        print(line)

TSV_INPUT_FILE = '../all-terms.tsv'
JSON_OUTPUT_FILE = '../stunda-terms.tsv'

def to_json():
    with open(TSV_INPUT_FILE, 'r') as infile:
        with open(JSON_OUTPUT_FILE, 'w') as outfile:
            for line in infile:
                fields = line.split('\t')
                if len(fields) > 4:
                    dict = {
                        'eng': fields[0].split(', '),
                        'swe': fields[1].split(', '),
                        'pos': fields[2],
                        'src': fields[3],
                        'row': fields[4].strip(),
                        'status': [0],                      # 0 = dumped, 1=manually added, 3=edited, 4=checked 
                        'comment': 'dumped from raw data'
                        }
                    json.dump(dict, outfile, indent=2, ensure_ascii=False)
        
if __name__ == '__main__':
    convert_all()  # initial conversion from data: save in TSV_INPUT_FILE, which is easier to edit
#    to_json()


