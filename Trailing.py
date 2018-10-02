import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Trailing",'r')
for test in test_cases:
	test = test.replace("\n","")
	if test:
		sides = test.split(",")
		if sides[1] in sides[0]:
			print 1
		else:
			print 0
test_cases.close()