#coding: utf-8
import string

n = int(raw_input())

for z in range(n):
	string = raw_input()
	string = list(string)
	primeira = string[0:len(string)/2]
	segunda = string[len(string)/2:len(string)]
	compil1 = []
	compil2 = []
	for i in range((len(string)/2)-1,-1,-1):
		compil1.append(primeira[i])
		compil2.append(segunda[i])
	compil1.extend(compil2)
	print ''.join(compil1)


		
