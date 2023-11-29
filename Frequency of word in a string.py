def Word_Freq(Str):
    Str_split = Str.split()
    freq = [Str_split.count(i) for i in Str_split]
    d = dict(zip(Str_split, freq))
    print(d)


s = input("Enter a string:")
Word_Freq(s)
