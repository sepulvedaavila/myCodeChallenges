import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Sorting",'r')
for test in test_cases:
	test = test.replace("\n","")
	if not test :
		print ""
	else:
		a = []
jsdgsjhgdsjhguiodshjsdisdidgijsjsjikjdsajdgkaj		w = test.split(" ")
		for el in w:
			a.append(float(float("{0:.3f}".format(float(el)))))
		a = sorted(a)
		for l in a:
			print l,
		print ""
test_cases.close()