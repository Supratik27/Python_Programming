def Even_Length(Str):
    l = []
    Str1 = Str.split()
    for i in Str1:
        if len(i) % 2 == 0:
            l.append(i)
    print(l)


S = input("Enter a String:")
Even_Length(S)
