#coding: utf-8

import math

def isPrime(n): 
	if n == 2: return True
	if n<= 1: return False
	if n%2 == 0: return False
	m = int(math.sqrt(n))

	for i in range(3, m+1, 2):
		if n % i == 0:
			return False
	return True
	

def crivo(x, y):
	

	lista = range(x,y+1)

	limite = int(math.sqrt(y))
	for j in range(limite+1):
		if isPrime(j):
			primo = j
			for i in range(len(lista)):
				if lista[i] % primo == 0:
					lista[i] = 0
			for i in range(len(lista)):
				if lista[i] != 0: lista[i] = 1
	print lista
	return lista		
		

## MAIN 

qtdcasos = int(raw_input())

for i in range(qtdcasos):
	nGemeos = 0
	cont = 0
	dados = raw_input().split()
	dados[0],dados[1] = int(dados[0]), int(dados[1])
	if dados[0] > dados[1]: dados[0],dados[1] = dados[1],dados[0]	
	lista = crivo(dados[0],dados[1])
			
	for i in range(len(lista)-1):
		if 
	
	print nGemeos	





