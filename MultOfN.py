import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/mOfAN", 'r')
for test in test_cases:
	num = test.split(",")
	a = int(num[0])
	b = int(num[1])
	i = 1
	if b < a:
		while b*i < a:
			i+=1
		print b*i
	else:
		pass
test_cases.close()