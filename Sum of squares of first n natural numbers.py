def SumOfSquares(N):
    Sum = 0
    for i in range(1, N + 1):
        Sum = Sum + i ** 2
    print("The sum of first natural numbers is %d" % Sum)


h = int(input("Enter the First n natural number to check its sum:"))
if h < 0:
    print("Invalid input")
else:
    SumOfSquares(h)
