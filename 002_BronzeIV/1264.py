vowels = ["a","e","i","o","u"]
while True :
	sentence = input().lower()
	if sentence == "#" : break
	result = 0
	for vowel in vowels:
		result += sentence.count(vowel)
	print(result)