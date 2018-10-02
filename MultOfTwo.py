import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/CrossMult",'r')
for test in test_cases:
	test = test.replace("\n","")
	sides = test.split("|")
	a = sides[0].split(" ")
	b = sides[1].split(" ")
	a.pop(len(a)-1)
	b.pop(0)
	for i in range(len(b)):
		print int(a[i])*int(b[i]),
	print ""
test_cases.close()