import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Rollercoaster",'r')
for test in test_cases:
	if not test or test == "\n":
		print ""
	else:
		test = test.replace("\n","")
		a = test.split(" ")
		i= 0
		lis=[]
		for words in a:
			for let in words:
				if i%2 == 0:
					lis.append(let.upper())
				else:
					lis.append(let.lower())
				i+=1
			lis.append(" ")
		for el in lis:
			sys.stdout.write(el)
		print ""
test_cases.close()