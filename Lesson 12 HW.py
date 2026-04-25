num = int(input("Enter a decimal number: "))
binary = []
while num > 0:
    remainder = num % 2
    binary.append(remainder)
    num = num // 2
reversed_binary = []
for i in range(len(binary)-1,-1,-1):
    for j in range(1):
        reversed_binary.append(binary[i])
print ("Binary number: ", end= "")
for bit in reversed_binary:
    print (bit, end= "")