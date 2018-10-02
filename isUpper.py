#---Using Python 2.#---Using Python 2.77
#---Case-swapping program
#-------------------------

import sys 

test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/isUpper",'r') #opens a file in a directory
for test in test_cases:
	print test.swapcase(), #for each line in file prints the line case-swapped

test_cases.close() #closes the file
