import sys
from datetime import datetime
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/TimeDiff",'r')
for test in test_cases:
	a = test.split(" ")
	a[1] = a[1].replace("\n","")
	FMT = '%X'
	res = datetime.strptime(a[0], FMT) - datetime.strptime(a[1], FMT)
	print res
test_cases.close()