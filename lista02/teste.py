#coding: utf-8

def VerificaSudoku():

	matrizColuna = []
	i = 0
	while i < 9:	
		for i in xrange(9):
			matrizColuna.append([])
			matriz = raw_input().split()  #este trecho resolve a soma nas linhas
		
			for m in range(len(matriz)): #str -> int	
				matriz[m] = int(matriz[m])
				matrizColuna[i].append(int(matriz[m]))
			if sum(matriz) != 45: 
				return False   #soma de cada linha
		i+=1

	for col in range(9):    #soma nas colunas
		soma = 0
		for lin in range(9):
			soma += matrizColuna[lin][col]
		if soma != 45: 
			return False

	#verifica matrizes menores
	
								
	
				
	return True	

#__MAIN

qtd = int(raw_input())


for i in range(qtd):
	
	if VerificaSudoku() == True: 
		print "Instancia %i" %(i+1)
		print "SIM\n"
	else: 
		print "Instancia %i" %(i+1)
		print "NÃO\n"
