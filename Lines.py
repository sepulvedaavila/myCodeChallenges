#Sorting program for lines in file|


import sys

test_cases = open("/home/carlos/Documents/CodeEval/try", 'r') #we open a file as readable
for test in test_cases: #for each line in file...
	i = 0 #initial index value per line
	words = test.split("\n") #we delete the unseen line-jumper
	while i < len(words)-1: #while the index is less than the size of the line...
		if words[i] > words[i+1]: #if the first element from the line is greater than the next...
			tmp = words[i] #we manually swap the elements
			words[i] = words[i+1]
			words[i+1] = tmp
		i+=1 #the index increases
	print words[len(words)-1] #we print the last element

test_cases.close() #closes the file
