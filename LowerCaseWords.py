import sys
test_cases = open("/home/carlos/Documents/testing/Words", 'r')
for test in test_cases:
    print (test.lower())
test_cases.close()