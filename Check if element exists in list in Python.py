myList = [1, 2, 3, 4, 5]
searchValue = 6
for item in myList:
    if item == searchValue:
        print("Item found!")
        break
    else:
        print("Item not found.")
        continue

