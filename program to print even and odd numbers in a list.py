def Even_list(List):
    even_list = []
    odd_list = []
    for number in List:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    print("the even numbers in the List are: %s" % even_list)
    print("the odd numbers in the List are: %s" % odd_list)


Li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even_list(Li)
