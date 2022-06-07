import ply.lex as lex

tokens = (
    'ADD',
    'MUL',
    'SUB',
    'NEG',
    'INC',
    'NUM'
)

t_ADD = r'add'
t_MUL = r'mul'
t_SUB = r'sub'
t_NEG = r'neg'
t_INC = r'inc'

def t_NUM(t):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s' " % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
