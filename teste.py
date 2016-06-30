atual = []
final = []

while True:
	atual = []
	tamanho = raw_input()
	if tamanho == "0 0":break
	tamanho = tamanho.split()
	for i in range(int(tamanho[1])):
		atual.append(int(tamanho[0]))
	final = raw_input().split()
	for i in range(len(final)):
		final[i] = int(final[i])

	cont = 0
	ligou = False	

	for i in range(int(tamanho[0])):
		ligou = False

		for i in range(len(atual)):
			if atual[i] != final[i]:
				atual[i] += -1
				ligou = True
			else: 
				if ligou == True: 
					cont+=1
					ligou = False
		
		if ligou == True: cont += 1	
	
	print cont





