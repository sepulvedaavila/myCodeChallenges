import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/MinCoin",'r')
for test in test_cases:
    test = test.replace("\n","")
    if test != "":
    	x = int(test)
    	y = 0
    	n = 0
    	m = 0
    	o = 0
    	while y != x:
    		
    		y = (n)+(m*3)+(o*5)
    	print (n+m+o)
test_cases.close()