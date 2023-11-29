def Find_Url(string):
    My_string = string.split()
    Url = []
    for Str in My_string:
        if Str.startswith("https:") or Str.startswith("http:"):
            Url.append(Str)
    return Url


string = input("Enter a string:")
print("Url:", Find_Url(string))