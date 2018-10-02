import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/LongestLines", 'r')
whole = test_cases.read().split("\n")
n = int(whole[0])
for i in range(1, len(whole)-1):
	for i in range(1, len(whole)-1):
		if len(whole[i]) > len(whole[i+1]):
			tmp = whole[i]
			whole[i] = whole[i+1]
			whole[i+1] = tmp
for j in range(n):
	print whole[len(whole)-1-j]
test_cases.close()