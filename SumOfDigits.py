import sys
test_cases = open("/home/carlos/Documents/CodeEval/try", 'r')
for test in test_cases:
	sumOf = 0
	for n in test:
		if (n == " ") or (n == "\n"):
			pass
		else:
			sumOf += int(n)
	print (sumOf)
test_cases.close()