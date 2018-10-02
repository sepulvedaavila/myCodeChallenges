import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/FirstUnR",'r')
for test in test_cases:
	wordTP = ""
	if not test or test == "\n":
		pass
	else:
		test = test.replace("\n","")
		
test_cases.close()