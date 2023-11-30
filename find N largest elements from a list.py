def n_list(List, n):
    List.sort()
    nth_element = List[-n]
    print("The element is %d" % nth_element)


List = [1, 2, 3, 4, 5, 6]
n = 3
n_list(List, n)