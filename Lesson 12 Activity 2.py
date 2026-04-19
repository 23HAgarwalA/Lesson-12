lowerrange = int(input("Please enter a lower range: "))
upperrange = int(input("Please enter an upper range: "))
print ("Prime numbers between", lowerrange, "and", upperrange, "are: ")
for num in range (lowerrange, upperrange + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print (num)