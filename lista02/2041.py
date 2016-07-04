#coding: utf-8

import string

def Godelito (qtd):
	letra = '3'
	for cont in range(qtd-1):
	

		saida = []
		it = 0
		A = letra[0]
		B = 0

		while True: 
	
			for i in range(it, len(letra)):
				if letra[i] == A:
					B += 1
				else:
					saida.append(str(B)+A)
					A = letra[i]
					B = 1
			it = i
			if len(letra) == it+1: 
				saida.append('1'+letra[i])
				break
	
		

		letra = ''.join(saida)

	
	return letra

#MAIN

while True:
    try:
        n = raw_input()
        print Godelito(int(n))
    except EOFError:
        break
