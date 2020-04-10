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
    '=' : 'ASSIGN'
}

tokens = [
    'INT',
    'FLOAT',
    'BOOLEAN',
    'STRING',
    'ID',
    'UNITARY_OPERATOR',
    'BINARY_OPERATOR',
    'SIGN',
    'ACCESS_TOKEN',
] + list(reserved.values())

t_BINARY_OPERATOR = r'\* | \/ | == | != | <= | >= | < | > | \+\+'
t_SIGN = r'\+ | \-'
t_UNITARY_OPERATOR = r'\~'

t_ignore = ' \t'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d*.\d+'
    t.value = float(t.value)
    return t

def t_BOOLEAN(t):
    r'true | false'
    if t.value == 'true':
        t.value = True
    elif t.value == 'false':
        t.value = False
    return t

def t_STRING(t):
    r'\'.*\''
    t.value = str(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_NUMBER(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
