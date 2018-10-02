import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/CapFirst", 'r')
for s in test_cases:
	lst = [word[0].upper() + word[1:] for word in s.split()]
	s = " ".join(lst)
	print s
test_cases.close()