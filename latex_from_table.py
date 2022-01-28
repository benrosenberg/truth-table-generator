# print out the latex tabular environment representation of a table 
# the table will be from a file called "table file" 
# this is so that it's not necessary to worry about the table's structure

def latexify(table_string, full_boolean = True):
    
    table = table_string.split('\n')
    for i in range(len(table)-1): table[i] += '\n'

    top_line = table[0]
    
    num_cols = top_line.count('\t')

    header = r'\begin{array}{' + (num_cols-1)*'c|' + 'c}\n'
    top_line = top_line.replace('\t', ' & ')[2:-1] + r'\\' + '\n'
    top_line = top_line.replace('AND', r'\land').replace('OR', r'\lor')
    top_line = top_line.replace('IMPLIES', r'\implies')
    top_line = top_line.replace('NOT', r'\neg') 
    top_line = top_line.replace('EQUALS', r'\iff') 
    header += top_line + r' \hline' + '\n'
    footer = r'\end{array}'

    middle = ''
    
    for row in range(1,len(table)):
        middle += table[row].replace('\t', ' & ')[2:-1] + r'\\' + '\n'

    middle = middle[:-3]
    
    middle = middle.replace('True', r'\text{True}').replace('False', r'\text{False}')
    if not full_boolean: 
        middle = middle.replace('True', 'T').replace('False', 'F')

    latex_out = header + middle + footer

    return latex_out
