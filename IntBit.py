import sys
import math
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/IntBit",'r')
for test in test_cases:
	a = bin(int(test))
	c = 0
	for one in a:
		if one == '1':
			c+=1
	print c
test_cases.close()
