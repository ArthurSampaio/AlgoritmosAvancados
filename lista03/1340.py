#coding: utf-8

#######MAIN
p = True
q = True
s = True
queue = []
stack = []
priority = []
while True:
	try:
		n = int(raw_input())

	except EOFError:
		break 
	
	queue, stack, priority = [],[],[]
	p, q, s = True, True, True
	for i in range(n):
		
		
		entrada = raw_input().split()
		if int(entrada[0]) == 1: 
			queue.append(int(entrada[1]))
			stack.insert(0,int(entrada[1]))
			priority.append(int(entrada[1]))
			
		else: 
			if queue[0] != int(entrada[1]): q = False
			if stack[0] != int(entrada[1]): s = False
			if max(priority) != int(entrada[1]): p = False
			queue.pop(0)
			stack.pop(0)
			priority.remove(max(priority))

	if (p and q and s) or (not p and q and s) or (p and not q and s) or (p and q and not s):
		print "not sure"
	elif (p and not q and not s): print "priority queue"
	elif (not p and not q and s): print "stack"
	elif (not p and q and not s): print "queue"
	else: print "impossible"
	
	
