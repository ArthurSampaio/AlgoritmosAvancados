#coding: utf-8

sz = raw_input()
n = int(sz)
soma = 0 
for i in range(len(sz)):
	soma += 10**i

print (len(sz)*(n+1) - soma)
