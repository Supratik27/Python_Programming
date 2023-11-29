def vowel_count(Str):
    vowels = set("aeiouAeiou")
    count = 0
    for i in Str:
        if i in vowels:
            count = count + 1
    print("No of vowels in the given string is: %d" % count)


Str = input("Enter the string to check for vowels count:")
vowel_count(Str)
