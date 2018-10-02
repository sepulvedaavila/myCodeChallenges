import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Scr", 'r')
for test in test_cases:
	words = test.split("\n")
	print words
test_cases.close()