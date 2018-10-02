qqimport sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/RightMost",'r')
for test in test_cases:
	if test == "\n" or not test:
		pass
	else:
		a = test.split(",")
		a[1] = a[1].replace("\n","")
		if a[1] in a[0]:
			print a[0].index(a[1])
		else:
			print "-1"
test_cases.close()