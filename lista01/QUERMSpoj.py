#coding: utf-8

teste = []
acerto = []
j = 1
while True: 
	n = int(raw_input())
	if n == 0: break 
	
	
	fila = raw_input().split()
	assert len(fila) == n
	for i in range(n): 
		if int(fila[i]) == i+1:
			teste.append(j)
			acerto.append(int(fila[i]))

	j += 1


			
for i in range(len(teste)):
	print "Teste %i" %teste[i]
	print "%i\n" %acerto[i]

	
