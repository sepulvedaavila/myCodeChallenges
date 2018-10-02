import sys
import math
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/HappyNum",'r')
cn = 1
notCool = [0, 4, 16, 20, 37, 42, 58, 89, 145]
repCas = []
for test in test_cases:
	test = test.replace("\n","")
	su = 0
	for a in test:
		su = pow(int(a),2)
		if su == 1:
			print 1
			break
		else:
			test = str(su)
test_cases.close()