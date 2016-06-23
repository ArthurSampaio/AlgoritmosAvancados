#coding: utf-8

valor = raw_input().split()
for i in range(len(valor)): 
	valor[i] = int(valor[i])
	assert valor [i] >= 0 and valor[i] <= 400
valor.sort()

if abs(valor[1]-valor[0]) < 200:
	c_coberto = 200 + abs(valor[1]-valor[0]) 
else: 
	c_coberto = 200 + 200


if abs(valor[2] - valor[1]) < 200:
	c_coberto += abs(valor[2] - valor[1])
else:
	c_coberto += 200



c_livre = 600-c_coberto

print c_livre*100
