import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/DecodeNums",'r')
listOfAl = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
for test in test_cases:
	c = 0
	test = test.replace("\n","")
	for el in test:
		for nums in listOfAl:
			if int(el) == nums:
				c+=1
	print c
test_cases.close()