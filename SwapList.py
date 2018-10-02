mport sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/SwapList",'r')
for test in test_cases:
	digg = []
	if not test or test == "\n":
		pass
	else:
		test = test.replace("\n","")
		list = test.split(":")
		list[0] = list[0].replace(" ","")
		
test_cases.close()