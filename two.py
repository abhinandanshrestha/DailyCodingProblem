#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

arr = [10,15,3,7,8]
k=13
diff=k-arr[0]
flag = False
for i in range(len(arr)):
    sum=arr[i]
    j=i+1
    for j in range(len(arr)):
        sum+=arr[j]
        if sum == k:
            flag = True
print(flag)


# Bonus: Can you do this in one pass?
# arr = [10,15,3,7,8]
# k=13
# diff=k-arr[0]
# flag = False
# i=1
# for i in range(len(arr)):
#     if diff == arr[i]:
#         flag=True
# print(flag)