#coding: utf-8

def  binsearch(seq, value):
	right = len(seq)
	left = 0
	if value < seq[0]: return -1
	if value > seq[-1]: return -1
	previous_center = -1
	while True:
		center = (right + left) / 2
		candidate = seq[center]
		if center == previous_center: return -1 
		if candidate == value: 
			return center
		elif valor < candidate: 
			right = center
		else:
			left = center
		
		previous_center = center
		

cont = 0
while True:
	cont += 1
	marbles = []	
	valores = []
	dados = raw_input().split()
	if dados[0] == '0' and dados[1] == '0': break
	n, q = int(dados[0]), int(dados[1])
	
	for i in range(n): 
		valor = int(raw_input())		
		marbles.append(valor)
	
	marbles.sort()


	for j in range(q):
		valor = int(raw_input())		
		valores.append(valor)


	print "CASE# %d:" %cont

	for j in range(len(valores)):
		valor = valores[j]

		if binsearch(marbles,valores[j]) != -1:
			print "%d found at %d" %(valores[j],binsearch(marbles, valor)+1)
		else: 
			print "%d not found" %valor

		

	
