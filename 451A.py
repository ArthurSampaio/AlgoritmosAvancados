#coding: utf-8

valor = raw_input().split()
a, b = int(valor[0]), int(valor[1])

if min(a,b) % 2 == 0:
	print "Malvika"
else: 
	print "Akshat"

