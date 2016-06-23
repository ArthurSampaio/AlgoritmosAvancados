#coding: utf-8

while True: 
	qtd_casos = int(raw_input())
	if qtd_casos == 0: break
	orig = raw_input().split()
	m, n = int(orig[0]), int(orig[1])
	for i in range(qtd_casos): 
		coord = raw_input().split()
		x, y = int(coord[0]), int(coord[1])
		
		if x == m or y == n: print "divisa"
		elif x > m: 
			if y > n: print "NE"
			else: print "SE"
		else: 
			if y > n: print "NO"
			else: print "SO"

	
		
