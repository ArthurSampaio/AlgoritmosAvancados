#conding: utf-8



def verificaEquacao(eq):
	eq = list(eq)
	aux = []
	aberto = 0
	fechado = 0
	for i in xrange(len(eq)):
		if eq[i] == "(":
			aux.append(eq[i])
			aberto += 1
		if eq[i] == ")":
			aux.append(eq[i])
			fechado += 1
	
	if aberto != fechado: return False
	if aux[0] == ")": return False
	if aux[-1] == "(": return False

	return True		


#####MAIN

while True:
    try:
        n = raw_input()
	if verificaEquacao(n): print "correct"
	else: print "incorrect"
       	
    except EOFError:
        break
	
	
