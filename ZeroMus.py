import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/ZeroMus",'r')
for test in test_cases:
	zTA = test.split(" ")
	a = []
	i = 0
	while i < len(zTA):
		print "I = "+str(i)
		numOf1 = 0
		for n in range(len(zTA[i+1])):
			numOf1 += 1
		if zTA[i] == '0':
			a.append(zTA[i+1])
		elif zTA[i] == '00':
			for x in range(len(zTA[i+1])):
				a.append("1")
		i+=2
	print a
test_cases.close()
