#coding: utf-8 

entrada = raw_input().split()
for i in range(len(entrada)): 
	entrada[i] = float(entrada[i])

assert 0.01 <= entrada[0] and entrada[0] <= 10
assert  0.01 <= entrada[1] and entrada[1] <= 10
assert 0.01 <= entrada[2] and entrada[2] <= 20
assert 0.01 <= entrada[3] and entrada[3] <= 20

if entrada[2]/entrada[0] > entrada[3]/entrada[1]:
	print "A"
else:
	print "G"

