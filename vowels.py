x=input()
list=['a','e','i','o','u','A',"E",'I','O','U']
if((x>='0')and(x<='9')):
	print("Invalid input")
if(((x>='a')and(x<='z'))or((x>='A')and(x<='Z'))):
	if x in list:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Invalid input")
