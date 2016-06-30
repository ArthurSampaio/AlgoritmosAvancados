#coding: utf-8

linha1 = raw_input().split()
escritorios = int(linha1[0])
esteveDoisDias = raw_input().split()
for i in range(len(esteveDoisDias)):
	esteveDoisDias[i] = int(esteveDoisDias[i])

aux = []

for i in range(escritorios):
	Id = int(raw_input())
	
	if Id in esteveDoisDias:
		aux.append(0)
	else: 
		aux.append(1)
		esteveDoisDias.append(Id)


