import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/IntBit",'r')
for test in test_cases:
	print str(test =='()' | test=='[]' | test=='{}')
test_cases.close()
