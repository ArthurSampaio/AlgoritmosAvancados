#coding: utf-8

def queue(inp, out):
	cont = 0
	for i in xrange(len(out)):
		if inp[i] == out[i]:
			cont += 1
	if cont > 0: return True
	return False

def stack(inp, out):
	j = 0
	cont = 0
	for i in xrange(len(out)):
		j -=1
		if inp[j] == out[i]:
			cont += 1
	if cont > 0: return True
	return False

def priorityQueue(inp, out):
	cont = 0
	for i in xrange(len(out)):
		if out[i] == max(inp):
			cont += 1
			inp.remove(max(inp))
	if cont > 0: return True
	return False


#######MAIN
inp = []
out = []
saida = []
a = 0
queue = 0
stack = 0
priority = 0
while True:
	try:
		n = int(raw_input())

	except EOFError:
		break 
	
	for i in range(n):
		entrada = raw_input().split()
		if int(entrada[0]) == 1: inp.append(int(entrada[1]))
		elif int(entrada[0]) == 2 and a >= 1:
			a = 0
			continue
		else: 
			out.append(int(entrada[1]))
			if queue(inp, out): saida.append("queue")
			if stack(inp, out): saida.append("stack")
			if priorityQueue(inp, out): saida.append("priority queue")
			a += 1
			
	
	
	if len(saida) == 0: print "impossible"
	elif len(saida) == 1: print saida[0]
	else: print "not sure"
	print saida
	
	inp, out, saida = [],[],[]

	 
