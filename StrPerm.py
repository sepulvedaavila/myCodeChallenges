import sys
import math
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/StrPerm", 'r')
for test in test_cases:
	m = test.replace("\n","")
	for i in range(len(m)):
		print m[i],
		for j in range(len(m)):
			if j!= i:
				print m[j],
		print ",",
	print ""

test_cases.close()