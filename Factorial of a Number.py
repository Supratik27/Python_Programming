fact = 1
num = int(input("Enter the no :"))
print("The no you entered is:%d" %num)
if num < 0:
    print("The factorial of the no does not exists")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact*i
    print("factorial of the no is",fact)


