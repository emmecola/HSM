#!/usr/bin/python
input_file = 'Huanan_PRJNA948658_ncbi_tax_analysis.txt'
i = open(input_file,'r')
mammals = False
for line in i.readlines():
    if line.startswith('Env_'):
        output_file = line.split(' ')[0] + '.txt'
        o = open(output_file,'w')
        mammals = False
    if line.startswith(20*' ' + 'Mammalia'):
        mammals = True
    elif mammals == True:
        if line.startswith(21*' '):
            o.write(line)
        else:
            mammals = False

i.close()
o.close()

