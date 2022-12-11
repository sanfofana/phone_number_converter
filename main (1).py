phonenumber = input("Enter phone number, please!: ").lower()
phonenumberMapping = {
	"1" : "one",
	"2" : "two",
	"3" : "three",
	"4" : "four",
	"5" : "five",
	"6" : "six",
	"7" : "seven"
}
output = ""

for phoneDigit in phonenumber:
	phonenumberMapping.get (phoneDigit, "!")
	output += phonenumberMapping.get(phoneDigit, "!") + " "

print(output)