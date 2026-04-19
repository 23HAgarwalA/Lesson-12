string = input("Please enter your own word/string of characters: ")
char = input("Please enter the character which you would like to know how many times is repeated in your own string: ")
i = 0
count = 0
while (i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
print ("The total number of times", char, "is repeated is:", count)
