arr = [5, 6, 15, 9, 50, 51, 95, 25, 74, 68]
# We will find the maximum value of the arr
Max = arr[0]
L = len(arr)
for i in range(1, L):
    if arr[i] > Max:
        Max = arr[i]

print("Maximum no in this array is", Max)

# We will find the minimum value of the arr
Min = arr[0]
for o in range(1, L):
    if arr[o] < Min:
        Min = arr[o]

print("Minimum no in this array is", Min)