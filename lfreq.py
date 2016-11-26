import sys

def letterFrequency(sentence,letter):
	sentence=list(sentence)
	count=0
	for i in range(len(sentence)):
		if sentence[i] == letter:
			count+=1
	return count

def sentenceFrequency(sentence):
	alphabeth=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '?', '/', '.', ',', '<', '>', '?', '[', ']', '{', '}', ':', ';']
	for i in range(len(alphabeth)):
		count = letterFrequency(sentence, alphabeth[i])
		if count > 0:
			print alphabeth[i], '=', count

def ascii2hex(l):
	for i in range(len(l)):
		print l[i].encode("hex"),

