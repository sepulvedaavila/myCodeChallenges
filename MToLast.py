import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/MtoLast", 'r')
for test in test_cases:
	nums = test.split(" ")
	m = int(nums[len(nums)-1])
	if m < (len(nums)):
		print nums[(len(nums)-1)-m]
test_cases.close()