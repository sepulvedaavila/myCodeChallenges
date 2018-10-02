import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Nums", 'r')
for test in test_cases:
	items = test.split(" ")
	items[len(items)-1] = items[len(items)-1].strip("\n")
	for item in items:
		num = float(item)
		i = 0
		while i < len(items)-1:
			if items[i] > items[i+1]:
				tmp = items[i]
				items[i] = items[i+1]
				items[i+1] = tmp
			i+=1
		print item,
test_cases.close()