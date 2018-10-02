def palindromeSearch(word):
	x = True
	l = len(word)
	lim = l/2
	for i in range(int(lim)):
		if(word[i] == word[l-1]):
			x = True
		else:
			x = False
		l-=1

	if x == True:
		return True
	else:
		return False

def primeFinder(num):
	coun = 0
	j = num
	while j > 0:
		if (num%j == 0):
			coun += 1
		j-=1
	if coun == 2:
		return True
	else:
		return False


for i in range(1000):
	val = ""
	if (primeFinder(i) == True):
		sPrime = str(i)
		val = palindromeSearch(sPrime)
		if (val == True):
			print(i)