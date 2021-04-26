# generate a truth table for some statements
from expression_evaluator import expr_eval
from latex_from_table import latexify
from collections import OrderedDict
import sys

def table(nv):
    arr = list([list([(j//(2**(nv-i-1)))%2 for j in range(2**nv)]) for i in range(nv)])

    for j in range(len(arr)):
        for k in range(2**nv):
            arr[j][k] = True if arr[j][k] == 0 else False

    return arr

def array_print(arr):
    s = ''
    for row in arr: 
        for i in row: s += '\t' + str(i)
        s += '\n'
    return s

def table_print(arr):
    # transpose
    for row in range(len(arr)):
        arr[row] = tuple(arr[row])
    arr = list(zip(*arr))
    return array_print(arr)

# augment matrix by adding another column 
# the column should be able to take values from previous rows
def augment(arr, expr):
    # first build up columns, then concatenate 
    # iterate through rows of table and evaluate each one
    
    arr.append([]) # new "column" to be added
    
    var_dict = OrderedDict()
    for v in variables: var_dict[v] = None

    for i in range(len(arr[0])):
        for v in range(len(variables)): var_dict[variables[v]] = arr[v][i]
        expression = expr_eval(expr, var_dict) 
        arr[len(arr)-1].append(expression)

    return arr

# get user input


if __name__ == '__main__':
    # basic argument parsing without argparse 
    # (there are only two arguments, argparse would be overkill)
    try:
        arg_1 = sys.argv[1]
        try: 
            arg_2 = sys.argv[2]    
        except:
            arg_2 = None
    except:
        arg_1, arg_2 = None, None

    variables = input('Enter variable names separated by spaces: ').split(' ')
    
    expr = input('Enter a logical expression of your variables: ')
    expressions = [expr]
    last = False
    while last != '':
        last = input('Enter another expression or hit <Return> to proceed: ')
        if last != '': expressions.append(last)

    s = ''
    for v in variables: 
        s += '\t' + v
    
    for e in expressions:
        s += '\t' + e
    
    s += '\n'
    
    out = table(len(variables))
    
    for e in expressions:
        out = augment(out,e)

    # no arguments
    if arg_1 is None and arg_2 is None:
        print(s + table_print(out))

    elif arg_1 == 'latex' and arg_2 is None:
        print(latexify(s + table_print(out)))

    elif arg_1 == 'latex' and arg_2 == 'short':
        print(latexify(s + table_print(out), False))

    else:
        print('Invalid arguments detected:', 
                'First argument: ' + arg_1,
                'Second argument: ' + arg_2,
                'Printing default output:', sep = '\n')
        print(s + table_print(out))

