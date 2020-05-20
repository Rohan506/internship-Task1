#Given input String of combination of the lower and upper case ,
# arrange characters in such a way that all lowercase letters should come first.
inputStr = "PyNaTive"
words = inputStr.split()
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print("\n arranging characters giving precedence to lowercase letters:")
print(sortedString)
