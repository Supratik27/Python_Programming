def Armstrong(num):
    str_num = str(num)
    n = len(str_num)
    Sum = 0
    for i in str_num:
        Sum = Sum + int(i) ** n
    if Sum == num:
        print("The number %d is Armstrong number" % num)
    else:
        print("The number %d is not Armstrong number" % num)


num = int(input("Enter the number to check if armstrong number:"))
Armstrong(num)
