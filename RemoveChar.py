import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/RemoveChar", 'r')
for test in test_cases:
	toRem = test.split(", ")
	charTo = toRem[1]
	newStr = toRem[0]
	for i in range (len(charTo)):
		newStr = newStr.replace(charTo[i], "")
	print newStr
test_cases.close()