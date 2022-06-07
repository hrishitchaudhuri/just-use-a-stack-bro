import ply.yacc as yacc

from lexer import tokens

def p_add(p):
	'PROG : ADD PROG PROG'
	p[0] = p[2] + p[3]
	
def p_mul(p):
	'PROG : MUL PROG PROG'
	p[0] = p[2] * p[3]
	
def p_sub(p):
	'PROG : SUB PROG PROG'
	p[0] = p[2] - p[3]
	
def p_neg(p):
	'PROG : NEG PROG'
	p[0] = -p[2]
	
def p_inc(p):
	'PROG : INC PROG'
	p[0] = p[2] + 1
	
def p_num(p):
	'PROG : NUM'
	p[0] = p[1]
	
def p_error(p):
	print("Syntax error.")
	

parser = yacc.yacc()

while True:
	try:
		s = input('REPL> ')
	except EOFError:
		break
		
	if not s:
		continue
		
	result = parser.parse(s)
	print(result)
