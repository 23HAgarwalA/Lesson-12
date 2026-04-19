num = int(input("Enter a number: "))
temp = num
count = 0
while temp > 0:
    count += 1
    temp //= 10
temp = num
mid = count // 2
if count % 2 == 1:
    for i in range (mid):
        temp //= 10
    print ("Product: ", temp % 10)
else: 
    for i in range (mid - 1):
        temp //= 10
    d1 = temp % 10
    temp //= 10
    d2 = temp % 10
    print ("Product: ", d1 * d2)