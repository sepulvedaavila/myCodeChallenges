import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/NameToDigit",'r')
for test in test_cases:
	numbs = test.split(";")
	a = []
	for n in range(len(numbs)):
		if numbs[n][0] == 'z':
			a.append(0)
		elif numbs[n][0] == 'o':
			a.append(1)
		elif numbs[n][0] == 't':
			if numbs[n][1] == 'w':
				a.append(2)
			else:
				a.append(3)
		elif numbs[n][0] == 'f':
			if numbs[n][1] == 'o':
				a.append(4)
			else:
				a.append(5)
		elif numbs[n][0] == 's':
			if numbs[n][1] == 'i':
				a.append(6)
			else:
				a.append(7)
		elif numbs[n][0] == 'e':
			a.append(8)
		elif numbs[n][0] == 'n':
			a.append(9)
	for i in a:
		sys.stdout.write(str(i))
	print ""
test_cases.close()