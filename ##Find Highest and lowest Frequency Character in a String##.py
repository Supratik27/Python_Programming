def max_freq(Str):
    My_string = "".join(Str.split())
    counter = {}
    for i in My_string:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    max_key = max(counter, key=counter.get)
    print(f"Character: {max_key} has the highest frequency of: {counter[max_key]}")


def min_freq(Str):
    My_string = "".join(Str.split())
    counter = {}
    for i in My_string:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    min_key = min(counter, key=counter.get)
    print(f"Character: {min_key} has the lowest frequency of: {counter[min_key]}")


Str = input("Enter a string to check the frequency of highest and lowest characters:")
max_freq(Str)
min_freq(Str)
