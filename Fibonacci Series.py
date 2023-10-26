# A series of number in which each number is the sum of last 2 preceding number
num = int(input("Enter the no till which you want to display your fibonacci series :"))
print("The no you entered is:", num)
a = 0
b = 1
print(a)
print(b)
for i in range (2, num+1):
    fib = a + b
    print(fib)
    a = b
    b = fib