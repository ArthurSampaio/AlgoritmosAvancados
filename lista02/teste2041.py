#coding: utf-8

import string

def Godelito (qtd):
	letra = '3'
	for cont in range(qtd):
	

		saida = []
		it = 0
		A = letra[0]
		B = 0

		while True: 
	
			for i in range(it, len(list(letra))):
				if letra[i] == A:
					B += 1
				else:
					saida.append(str(B)+A)
					break
			it = i
			A = letra[i]
			B = 0
			if len(letra) == it+1: 
				saida.append('13')
				break
		letra = ''.join(saida)
	return letra

#MAIN

def main():
	dado = int(raw_input())
	print Godelito(dado-1)

if __name__ == '__main__':
	main()

