import random

char_n = ""

while(char_n == "" or int(len(char_n)) > 15):
	print("Please enter a name: ")
	char_n = input()
	if(int(len(char_n)) > 15):
		print("Must be less than 15 characters.")
		
print(char_n)