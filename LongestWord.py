import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Scr", 'r')
for test in test_cases:
	test = test.replace("\n","")
	words = test.split(" ")
	lon = ""
	for word in words:
		if len(word) > len(lon):
			lon = word
	print lon
test_cases.close()