import sys
def isInt(s):
    try:
    	b = int(n)
        return True
    except ValueError:
        return False

test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/MixedList",'r')
for test in test_cases:
	test.replace("\n","")
	if not test:
		break
	else:
		numList = []
		strList = []
		test = test.replace("\n","")
		a = test.split(",")
		for n in a:
			if isInt(n) == True:
				numList.append(n)
			if isInt(n) == False:
				strList.append(n)
		if len(strList) > 0:
			sys.stdout.write(strList[0])
			for	i in range(1,len(strList)):
				sys.stdout.write(","+strList[i])
		
		if len(numList) > 0:
			if len(strList) > 0:
				sys.stdout.write("|")
			for nm in range(len(numList)):
				if nm == 0:
					sys.stdout.write(numList[nm])
				else:
					sys.stdout.write(","+numList[nm])
		print ""
test_cases.close()