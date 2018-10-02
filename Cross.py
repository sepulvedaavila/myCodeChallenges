import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Sorting",'r')
for test in test_cases:
	test = test.replace("\n","")
	w = test.split(" ")
	a = sorted(w)
	for items in a:
		print items,
	print ""
test_cases.close()