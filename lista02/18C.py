#coding: utf-8
# Arthur Sampaio, 18C, CodeForces

len_stripe = int(raw_input())
stripe = raw_input().split()

S1 = 0
S2 = 0
cont = 0

#converte
for i in range(len(stripe)): 
	stripe[i] = int(stripe[i])
	S2 += stripe[i]

for j in range(len(stripe)-1):
	S1 += stripe[j]
	S2 -= stripe[j]
	if S1 == S2:
		cont += 1
	
print cont

