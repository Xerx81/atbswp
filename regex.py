import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
if mo:
    print('Phone number found: ' + mo.group())
    areacode, phonenumber = mo.groups() 
    print('Area code: ' + areacode)
    print('Phone number: ' + phonenumber)

    numbers = phoneNumRegex.findall("the numbers are 415-555-4242 and 415-384-4899")
    print(numbers[1][0])

print("\n")

# Matching multiple groups with pipe
print("# Using Pipe '|'")
heroRegex = re.compile(r'Batman|Superman')
mo = heroRegex.search("Batman and Superman")
if mo:
    print(mo.group())  # Whichever word appears first in string is printed

batRegex = re.compile(r'Bat(man|mobile|suit|rang)')
mo = batRegex.search("Joker stole Batmobile")
if mo:
    print(mo.group())
    print(mo.group(1))
print("\n")

# Optional matching using '?'
print("Optional matching using '?'")
batRegex2 = re.compile(r"Bat(wo)?man")
mo1 = batRegex2.search("The adventures of Batman")
mo2 = batRegex2.search("the adventures of Batwoman")
if mo1 and mo2:
    print(mo1.group())
    print(mo2.group())
