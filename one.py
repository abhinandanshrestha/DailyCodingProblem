# Given an array of integers, return a new array such that each element at index i 
# of the new array is the product of all the numbers in the original array except the one at i.

arr = [1,2,3,4,5]
newarr=[]
mul=1
n = len(arr)
for i in range(n):
    for j in range(n):
        if j != arr.index(arr[i]):
            mul=mul*arr[j]
    newarr.append(mul)
    mul = 1
print(newarr)