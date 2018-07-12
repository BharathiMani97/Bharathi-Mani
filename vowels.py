x=input()
list=['a','e','i','o','u','A',"E",'I','O','U']
if((x>='0')and(x<='9')):
	print("Invalid input")
elif x in list:
	print("Vowels")
else:
	print("consonant")
