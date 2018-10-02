import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Intersection",'r')
for test in test_cases:
	ls = test.split(";")
	a = ls[0].split(",")
	b = ls[1].split(",")
	for el in a:
		if b.index(el):
			print "Yes"
test_cases.close()