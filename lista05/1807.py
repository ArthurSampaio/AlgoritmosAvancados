#coding: utf-8

lista = [[1],[1,1,1]]

n = int(raw_input())
n -= 2
for i in range(n):
	linha = [1]
	for j in range(0,len(lista[i])-1):
		if (j == 1):
			linha.append(lista[i][j] + lista[i][j+1])

		elif (j == len(lista[i])-2):
			linha.append(lista[i][j] + lista[i][j-1])

		else:
			linha.append(lista[i][j-1] + lista[i][j] + lista[i][j+1])
			print "a linha", linha
		linha.append(1)
		lista.append(linha)


for i in range(len(lista)):
	print lista[i]
