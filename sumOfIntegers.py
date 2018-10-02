import sys
test_cases = open("/home/carlos/Documents/CodeEval/try", 'r')
sum = 0
for test in test_cases:
    num = int(test)
    sum+=num
test_cases.close()
print sum
