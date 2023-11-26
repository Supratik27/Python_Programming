# In this program we will check if a number is in fibonacci series or not
# For a number to be in a fibonacci series it should follow the below equation:
# (5 * square of number + 4) or ((5 * square of number - 4) should be a perfect square
import math


def Perfect_Square(num):
    s = int(math.sqrt(num))
    return s * s == num


def Is_Fib(num):
    if Perfect_Square(5 * (num ** 2) + 4) or Perfect_Square(5 * (num ** 2) - 4):
        print("The %d is a fibonacci number" % num)
    else:
        print("The %d is not a fibonacci number" % num)


n = int(input("Enter the number to check if the number is a fibonacci number:"))
if n < 0:
    print("Invalid number entered!!")
else:
    Is_Fib(n)

