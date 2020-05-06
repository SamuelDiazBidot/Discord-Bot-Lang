import ply.lex as lex
import ply.yacc as yacc

from intermediateCode import run, makeFile

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'fn' : 'FN',
    'command' : 'COMMAND',
    'try' : 'TRY',
    'ret' : 'RET',
    'global' : 'GLOBAL',
    'catch' : 'CATCH',
    'token' : 'TOKEN'
}

tokens = [
    'FLOAT',
    'INTEGER',
    'BOOLEAN',
    'STRING',
    'ID',
    'UNITARY_OPERATOR',
    'BINARY_OPERATOR',
    'SIGN',
] + list(reserved.values())

t_SIGN = r'\+ | \-'
t_UNITARY_OPERATOR = r'\~'

t_ignore = ' \t'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOLEAN(t):
    r'true | false'
    if t.value == 'true':
        t.value = True
    elif t.value == 'false':
        t.value = False
    return t

def t_STRING(t):
    r'\'[^\']*\''
    t.value = str(t.value)
    return t

def t_BINARY_OPERATOR(t):
    r'\* | \/ | == | != | <= | >= | < | > | and | or'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_NUMBER(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

literals = ['.',',', ';', ':' ,'=', '{', '}', '(', ')', '[', ']']

lex.lex()

def p_run(p):
    '''
    run : program
    '''
    makeFile(p[1])

def p_program(p):
    '''
    program : program function
            | program function_call
            | program python_function_call
            | program variable
            | program token
            | function
            | function_call
            | python_function_call
            | variable
            | token
    '''
    if len(p) == 3:
        p[0] = ('program', p[1], p[2])
    else:
        p[0] = p[1]

def p_function(p):
    '''
    function : FN id '(' parameter ')' '{' body '}'
             | COMMAND id '(' parameter ')' '{' body '}'
    '''
    p[0] = (p[1], p[2], p[4], p[7] )

def p_token(p):
    '''
    token : TOKEN '(' string ')'
    '''
    p[0] = ('token', p[3])

def p_function_call(p):
    '''
    function_call : id '(' term_list ')' 
    '''
    p[0] = ('function_call', p[1], p[3])

def p_python_function_call(p):
    '''
    python_function_call : '.' id '(' term_list ')'
    '''
    p[0] = ('python_function_call', p[2], p[4])

def p_parameter(p):
    '''
    parameter : id ',' parameter
              | id
              | empty
    '''
    if len(p) == 4:
        p[0] = ('parameter', p[1], p[3])
    else:
        p[0] = ('parameter', p[1])

def p_body(p):
    '''
    body : body exp
         | body variable
         | body return
         | body global
         | body function_call
         | body python_function_call
         | function_call
         | python_function_call
         | exp
         | variable
         | return
         | global
    '''
    if len(p) == 3:
        p[0] = ('body', p[1], p[2])
    else:
        p[0] = ('body', p[1])

def p_exp(p):
    '''
    exp : term binop exp
        | term
        | IF exp '{' body '}' ELSE '{' body '}'
        | IF exp '{' body '}'
        | TRY '{' body '}' CATCH '{' body '}'
    '''
    if len(p) == 10:
        p[0] = ('if_exp', p[2], p[4], p[8])
    elif len(p) == 9:
        p[0] = ('try_exp', p[3], p[7])
    elif len(p) == 6:
        p[0] = ('if_exp', p[2], p[4])
    elif len(p) == 4:
        p[0] = ('binop_exp', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_variable(p):
    '''
    variable : id '=' exp 
    '''
    p[0] = ('variable', p[1], p[3])

def p_return(p):
    '''
    return : RET id
    '''
    p[0] = ('return', p[2])

def p_global(p):
    '''
    global : GLOBAL term_list
    '''
    p[0] = ('global', p[2])

def p_term_map(p):
    '''
    term_map : term ':' term ',' term_map
             | term ':' term
    '''
    if len(p) == 6:
        p[0] = ('term_map', p[1], p[3], p[5])
    else:
        p[0] = ('term_map', p[1], p[3])

def p_term_list(p):
    '''
    term_list : term_list ',' term
              | term
    '''
    if len(p) == 4:
        p[0] = ('term_list', p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''
    term : unop term
         | number
         | boolean
         | string
         | function_call
         | python_function_call
         | id
         | list
         | dict
         | empty
    '''
    if len(p) == 3:
        p[0] = ('unop_term', p[1], p[2])
    else:
        p[0] = p[1]

def p_unop(p):
    '''
    unop : SIGN
         | UNITARY_OPERATOR
    '''
    p[0] = p[1]

def p_binop(p):
    '''
    binop : SIGN
          | BINARY_OPERATOR
    '''
    p[0] = p[1]

def p_dict(p):
    '''
    dict : '{' term_map '}'
         | '{' empty '}'
    '''
    p[0] = ('dict', p[2])

def p_list(p):
    '''
    list : '[' term_list ']'
    '''
    p[0] = ('list', p[2])

def p_number(p):
    '''
    number : FLOAT
           | INTEGER
    '''
    p[0] = ('number', p[1])

def p_boolean(p):
    '''
    boolean : BOOLEAN
    '''
    p[0] = ('boolean', p[1])

def p_string(p):
    '''
    string : STRING
    '''
    p[0] = ('string', p[1])

def p_id(p):
    '''
    id : ID
    '''
    p[0] = ('id', p[1])

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    print('error in: ', p)

def make_parser():
    parser = yacc.yacc()
    return parser