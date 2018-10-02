import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/PentulWord",'r')
for test in test_cases:
	words = test.split(" ")
	for n in range(len(words)-1):
		if words[n] > words [n+1]:
			tmp = words[n]
			words[n] = words[n+1]
			words[n+1] = tmp
		print words[len(words)-1]
test_cases.close()