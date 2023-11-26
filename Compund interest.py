def compound_interest(p, r, t):
    amount = p*(pow((1 + r / 100), t))
    ci = amount - p
    print("Compound interest is Rs %d" % ci)


p = int(input("Enter the principle amount"))
r = int(input("Enter the rate of interest"))
t = int(input("Enter the time in years"))
compound_interest(p, r, t)
