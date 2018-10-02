import sys
import re
test_cases = open("/home/carlos/Documents/testing/Reverse", 'r')
for test in test_cases:
	br = test.split(" ")
	br[len(br)-1] = br[len(br)-1].strip("\n")
	i = 0
	j = len(br)-1
	for a in range(len(br)/2):
		tmp = br[i]
		br[i] = br[j]
		br[j] = tmp
		j-=1
		i+=1
	print " ".join(br)
test_cases.close()