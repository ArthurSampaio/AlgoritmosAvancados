#coding: utf-8

entrada = raw_input().split()
a,b = int(entrada[0]), int(entrada[1])

if max(a,b) % min(a,b) == 0:
	print "Sao Multiplos"
else:
	print "Nao sao Multiplos"

