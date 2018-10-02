import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Stack", 'r')
for test in test_cases:
    test = test.replace("\n","")
    if test != "":
    	a = test.split(" ")
        i = len(a)-1
        while i >= 0:
            print a[i],
            i-=2
        print ""
test_cases.close()
