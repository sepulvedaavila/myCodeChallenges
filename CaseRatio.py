import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/CaseRatio",'r')
for test in test_cases:
	test = test.replace("\n","")
	if test:
		uC = 0
		lC = 0
		for let in test:
			if let.isupper():
				uC += 1
			else:
				lC += 1
		lowerPer = (float(lC)*100)/len(test)
		upperPer = (float(uC)*100)/len(test)
		print "lower: {0:.2f}".format(lowerPer)+" upper: {0:.2f}".format(upperPer)
test_cases.close()