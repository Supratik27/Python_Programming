# Approach 1: using temporary variable
li = [2, 5, 7, 9, 4, 7]
print("Original list", li)
temp = li[0]
li[0] = li[-1]
li[-1] = temp
print("List after swapping with temporary variable", li)

# Approach 2: using pop()
li1 = [3, 5, 7, 9, 5, 6]
print("Original list", li1)
first = li1.pop(0)
last = li1.pop(-1)
li1.insert(0, last)
li1.append(first)
print("List after swapping with pop()", li1)

# Swapping the 2nd and 5th element of the list
li2 = [9, 6, 7, 5, 3, 8, 9, 0, 1]
print("The original list", li2)
second = li2.pop(1)
fifth = li2.pop(4)
li2.insert(1, fifth)
li2.insert(4, second)
print("List after swapping the 2nd and 5th element", li2)
