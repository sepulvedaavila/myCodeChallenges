import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/ReadMore",'r')
for test in test_cases:
	test = test.replace("\n","")
	if not test:
		pass
	else:
		if (len(test) < 56):
			print (test)
		else:
			if (test[37]==" "):
				print (test[0:37]+"... <Read More>")
			else:
				print (test[0:38]+"...<Read More>")
test_cases.close()