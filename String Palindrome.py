def Palindrome(s):
    str_rev = s[::-1]
    if str_rev == s:
        print("The given string %s is a palindrome" % s)
    else:
        print("The given string %s is not a palindrome" % s)


s = input("Enter a string to check palindrome:").lower()
Palindrome(s)
