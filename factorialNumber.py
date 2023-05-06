from math import factorial


num = int(input("Enter the Number to get the Factorial.\n"))

factorial = 1

if num < 0:
    print("Factorial of negative number does not exist")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num+1):
        factorial *=i
    print("The factorial of %d is %d" %(num, factorial))