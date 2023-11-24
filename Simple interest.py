def simple_interest(p, r, t):
    return (p * r * t) / 100


p = int(input("Enter the principle amount"))
r = int(input("Enter the rate of interest"))
t = int(input("Enter the time in years"))
print("The Simple interest is Rs %d" % simple_interest(p, r, t))
