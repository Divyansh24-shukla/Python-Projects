# ARMSTRONG NUMBER PROGRAM

Number = int(input("Enter a Number to check wheather it is a Armstrong number or not.\n"))

length = len(str(Number))
print(length)
sum = 0

Number1 = Number
while Number1 > 0:
    digit = Number1 % 10
    sum += digit ** length
    Number1 //= 10

if Number == sum:
    print(Number, "is a Armstrong Number.")
else:
    print(Number, "is not a Armstrong Number.")