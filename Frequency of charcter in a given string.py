def freq_Str(Str):
    li = list(Str)
    freq = [li.count(ele) for ele in li]
    d = dict(zip(li, freq))
    print(d)


Str = input("Enter a String:")
freq_Str(Str)
