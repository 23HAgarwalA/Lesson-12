string = input("Please enter a string of characters: ")
i = 0
count = 0
for i in range (i, len(string)):
    if (string[i] in "aeiou" ):
        count = count + 1
    i = i + 1
print ("The total number of vowels in your string is", count)