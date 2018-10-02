import sys
test_cases = open("/home/carlos/Documents/CodeEval/TestFiles/Pangrams",'r')
for test in test_cases:
	if not test:
		pass
	else:
		alph = ['a','b','c','d','e','f','g','h','i','j','k',
		'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
		matches = []
		test = test.replace("\n","")
		for el in test:
			matcheshttps://www.codeeval.com/following/.append(el.lower())
		a = list(set(alph) - set(matches))
		if not a:
			print "NULL",
		else:
			a = sorted(a)
			for l in a:
				sys.stdout.write(l)
		print ""
test_cases.close()