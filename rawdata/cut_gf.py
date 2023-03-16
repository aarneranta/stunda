
GF_FILE='gf-termsEngSwe.tsv'

with open(GF_FILE) as file:
    for line in file:
        fields = line.split('\t')
        fun = fields[0]
        eng = fields[1].split(',')
        swe = fields[2].split(',')
        if fun.endswith('CNCSE'):
            entry = [[eng[0], eng[2]], [swe[0], swe[4], swe[6]], 'N']
        elif fun.endswith('NCSE'):
            entry = [[eng[0], eng[2]], [swe[0], swe[2], swe[4]], 'N']
        elif fun.endswith('APCSE'):
            entry = [[eng[0]], [swe[0], swe[1], swe[2]], 'A']
        elif fun.endswith('VCSE'):
            entry = [[eng[0], eng[4], eng[2]], [swe[6], swe[2], swe[8]], 'V']
        print('\t'.join([','.join(entry[0]),','.join(entry[1]), entry[2]]))
    

