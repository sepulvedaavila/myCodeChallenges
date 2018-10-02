import sys
test_case = open("/home/carlos/Documents/CodeEval/TestFiles/HexToDec", 'r')
for test in test_case:
	print int(test,16)
test_case.close()