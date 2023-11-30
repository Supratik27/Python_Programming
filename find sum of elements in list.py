def sum_list(List):
    Sum = 0
    for i in List:
        Sum = Sum + i
    print("The Sum of the list is: %d" % Sum)


List = [10, 20, 30, 40, 50]
sum_list(List)
min_list = min(List)
print(min_list)
max_list = max(List)
print(max_list)