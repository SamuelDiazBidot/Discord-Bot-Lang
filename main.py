import ply.lex as lex
import ply.yacc as yacc
import sys

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'fn' : 'FN',
    'command' : 'COMMAND',
    'handler' : 'HANDLER',
    'try' : 'TRY',
    'catch' : 'CATCH',
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
    r'\* | \/ | == | != | <= | >= | < | > | and | or | \+\+'
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

literals = [',', ';', ':' ,'=', '{', '}', '(', ')', '[', ']']

lexer = lex.lex()

def p_run(p):
    '''
    run : program
    '''
    print(p[1])
    run(p[1])

def p_program(p):
    '''
    program : program function
            | program function_call
            | program variable
            | function
            | function_call
            | variable
    '''
    if len(p) == 3:
        p[0] = ('program', p[1], p[2])
    else:
        p[0] = p[1]

def p_function(p):
    '''
    function : FN id '(' parameter ')' '{' body '}'
             | COMMAND id '(' parameter ')' '{' body '}'
             | HANDLER id '(' parameter ')' '{' body '}'
    '''
    p[0] = (p[1], p[2], p[4], p[7])

def p_function_call(p):
    '''
    function_call : id '(' term_list ')' 
    '''
    p[0] = ('fuction_call', p[1], p[3])

def p_parameter(p):
    '''
    parameter : id ',' parameter
              | id
              | empty
    '''
    if len(p) == 4:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

def p_body(p):
    '''
    body : body exp
         | body variable
         | exp
         | variable
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

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

def p_term_map(p):
    '''
    term_map : term ':' term ',' term_map
             | term ':' term
    '''
    if len(p) == 6:
        p[0] = (p[1], p[3], p[5])
    else:
        p[0] = (p[1], p[3])

def p_term_list(p):
    '''
    term_list : term_list ',' term
              | term
    '''
    if len(p) == 4:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''
    term : unop term
         | number
         | boolean
         | string
         | function_call
         | id
         | list
         | dict
         | empty
    '''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_unop(p):
    '''
    unop : SIGN
         | UNITARY_OPERATOR
    '''
    p[0] = ('unOp', p[1])

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

parser = yacc.yacc()

s = '''
x = 1
token('xxxxx')
handler sayHello(message) {
    content = getContent(message)
    if matches('*hello', content) {
        send('hello there')
    }
}
'''

t = '''
x = 1
y = 'hello'
fn x() {
    x
}
z = 3
'''

def run(p):
    if p[0] == 'program':
        run(p[1])
        run(p[2])
    elif p[0] == 'variable':
        print(run(p[1]), '=' , run(p[2]))
    elif p[0] == 'fn':
        print('def', run(p[1]), '(', '):')
    elif p[0] == 'id':
        return str(p[1])
    elif p[0] == 'number':
        return str(p[1])
    elif p[0] == 'string':
        return str(p[1])

parser.parse(t)