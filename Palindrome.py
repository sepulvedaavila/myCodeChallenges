word =raw_input("Which word do you want to check for a palindrome?\n>> ")
x = True
l = len(word)
lim = l/2
for i in range(int(lim)):
	if(word[i] == word[l-(i+1)]):
		x = True
	else:
		x = False
	l-=1

if x == True:
	print "It's a palindrome!"
else:
	print "It's not a palindrome"
