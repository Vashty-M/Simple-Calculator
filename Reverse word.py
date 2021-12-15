## initializing the string
string = "Determination, hardwork and passion leads to success"

## splitting the string on space
words = string.split(" ")
## reversing the words using reversed() function
print(words)

words=words[-1::-1]

print(words)

Reversedstr=" ".join(words)

print(Reversedstr)
