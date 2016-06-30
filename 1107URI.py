#coding: utf-8

def ContaLaser(atual, final):
	cont = 0
	ligou = False	
	loop = atual[0] - min(final)

	for i in range(loop):
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
	
	return cont
	

def main():

	while True:
		atual = []
		tamanho = raw_input()
		if tamanho == "0 0":break
		tamanho = tamanho.split()
		final = raw_input().split()
		for i in range(int(tamanho[1])):
			atual.append(int(tamanho[0]))
			final[i] = int(final[i])
		
		print ContaLaser(atual,final)
		

if __name__ == '__main__':
	main()		
		
