# evaluate a logical expression
import sys

def rpn_producer(expr, var_list):
    token_list = expr.split(' ')

    operation_stack = []
    output_queue = []

    while token_list != []:
        t = token_list.pop(0)
        if is_var(t, var_list): output_queue.append(t)
        if is_operator(t):
            while operation_stack != [] and has_greater_precedence(t, operation_stack[-1]):
                output_queue.append(operation_stack.pop())
            operation_stack.append(t)
        if t == '(': operation_stack.append(t)
        if t == ')':
            while operation_stack[-1] != '(':
                output_queue.append(operation_stack.pop())
            operation_stack.pop()
    while operation_stack != []:
        output_queue.append(operation_stack.pop())

    return output_queue

def is_var(t, var_list):
    return t in var_list

def is_operator(t):
    return t in ['NOT', 'AND', 'OR', 'IMPLIES', 'EQUALS']

def has_greater_precedence(t, other):
    
    precedence_dict = {
            'NOT' : 1,
            'AND' : 2,
            'OR'  : 3,
            'IMPLIES' : 4,
            'EQUALS'  : 5
    }
   
    if other == '(': return False

    if t not in precedence_dict or other not in precedence_dict:
        raise TypeError('Unknown operator!')
    
    return precedence_dict[t] > precedence_dict[other]

def rpn_eval(rpn_list, var_list, var_dict):
    binary_operators = ['AND', 'OR', 'IMPLIES', 'EQUALS']
    unary_operators = ['NOT']
    
    stack = []
    queue = rpn_list

    t = 0
    while t < len(queue):
        if is_var(queue[t], var_list): stack.append(queue[t])
        elif queue[t] in binary_operators:
            a = stack.pop()
            b = stack.pop()
            stack.append(bin_op(a,b,queue[t], var_dict))
        elif queue[t] in unary_operators:
            a = stack.pop()
            stack.append(unary_op(a,queue[t], var_dict))
        t += 1

    return stack[0]

def bin_op(a,b,op, var_dict):
    if a not in [True, False]:
        a = var_dict[a]
    if b not in [True, False]:
        b = var_dict[b]

    if op == 'AND': return a and b
    if op == 'OR' : return a or  b
    if op == 'IMPLIES': return implies(b,a)
    if op == 'EQUALS' : return a == b

def unary_op(a, op, var_dict):
    if a not in [True, False]:
        a = var_dict[a]

    if op == 'NOT': return not a

def implies(P, Q):
    return (not P) or Q

def expr_eval(expr, var_dict):
    var_list = list(var_dict.keys())
    
    rpn = rpn_producer(expr, var_list)
    out = rpn_eval(rpn, var_list, var_dict)
    return out

