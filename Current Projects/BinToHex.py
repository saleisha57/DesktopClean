# Binary to Hexadecimal convertion

# Dictionary for converting binary to hexadecimal/
Dict = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9", "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}

# User is prompted for input for the intial string of binary in groups of 4.
def getBinary():
	inBin = ""
	goagain = True
	while goagain:
		continuein = ""
		userin = ""		
		while len(userin) != 4:
			userin = input("Enter a string of 4 binary digits: ")
			if len(userin) != 4:
				print("Must have 4 binary digits to continue")
		inBin += userin
		continuein = input("Enter another group of 4 binary? (y/n) ")
		if continuein != "y":
			goagain = False
			return inBin

# Separates the initial string of binary into sections of 4 in a list.
def splitBinary(inBin):
	sendBin = []
	holder = ""
	while len(inBin) > 0:
		for x in range(0, 4):
			if len(holder) < 4:
				holder += inBin[x]
		sendBin.append(holder)
		holder = ""
		inBin = inBin[4:]
	return sendBin

# Initial binary is generated.
initialBinary = getBinary()	
print("\nBinary: "+initialBinary)

# Binary is separated.
sepBin = splitBinary(initialBinary)

# Iterates through the list of separated binary and prints corresponding hex value.
hexnumber = ""
for x in sepBin:
	for key, val in Dict.items():
		if x == key:
			hexnumber += val
print("\nHexadecimal: "+hexnumber+"\n")