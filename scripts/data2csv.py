import pandas

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


def convert_all():
    lines = []
    for file in data_files:
            for line in data2csv(file):
                fields = line.split('\t')
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


if __name__ == '__main__':
    convert_all()


