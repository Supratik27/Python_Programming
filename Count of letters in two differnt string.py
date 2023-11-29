def letter_count(Str1, Str2):
    Str1 = set(Str1)
    Str2 = set(Str2)
    matched_letter = Str1 & Str2
    print("The No of matched letter is:", str(len(matched_letter)))
    print(matched_letter)


Str1 = input("Enter the 1st String:")
Str2 = input("Enter the 2nd String:")
letter_count(Str1, Str2)