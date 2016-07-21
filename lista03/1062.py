#coding: utf-8

tam = 0

pilha = []




while True:
	n = int(raw_input())
	if n == 0: break	

	while True: 
		saida = raw_input().split()
		if saida[0] == "0": break

		for i in range(len(saida)): saida[i] = int(saida[i])
		tam = 0
		j = 1

		#push 
		tam += 1
		pilha[tam-1] = j
		#fim do push
		j += 1
		falhou = False
		for i in range(n):
			while pilha[tam-1] != saida[i] and j <= n:
				#push 
				tam += 1
				pilha[tam-1] = j
				#fim do push
				push += 1
			if pilha[tam-1] == saida[i]: 
				#POP
				if tam > 0: tam -= 1
			else:
				print "No\n"
				falhou = True
				break
		if not falhou: print "Yes\n"
print "\n"
			
		
