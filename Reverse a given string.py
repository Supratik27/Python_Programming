def str_rev(s):
    rev = str.split(s)[::-1]
    l = []
    for i in rev:
        l.append(i)
    print(" ".join(l))


s = input("Enter a string:")
str_rev(s)
