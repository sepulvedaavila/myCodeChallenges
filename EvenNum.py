import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Nums", 'r')
for test in test_cases:
	print int(int(test)%2 == 0)
test_cases.close()