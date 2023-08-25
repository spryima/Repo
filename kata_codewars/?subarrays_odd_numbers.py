# Subarrays with an odd number of odd numbers
# https://www.codewars.com/kata/6155e74ab9e9960026efc0e4/python

# Implement a function which takes an array of nonnegative integers and returns the number of subarrays 
# with an odd number of odd numbers. Note, a subarray is a contiguous subsequence.

# Example
# Consider an input:

# [1, 2, 3, 4, 5]
# The subarrays containing an odd number of odd numbers are the following:

# [1, 2, 3, 4, 5], [2, 3, 4], [1, 2], [2, 3], [3, 4], [4, 5], [1], [3], [5]
# The expected output is therefore 9.

# Test suite
# 100 random tests, with small arrays, 5 <= size <= 200, testing the correctness of the solution.

# 10 performance tests, with arrays of size 200 000.

# The expected output for an empty array is 0, otherwise 
# the content of the arrays are always integers k such that 0 <= k <= 10000.



def solve(arr):
    length_arr = len(arr)
    if length_arr == 0:
        return 0
    count = 0
    arrays_list = lst = [x for x in range(sum([x for x in range(len(arr)+1)]))]

# перебор всіх можливих списків 
    for length in range(length_arr):  # length - довжина варіанту (1 символьний, 2 символьний і тд.)
        for num in range(length_arr - length):  # к-ть length-символьних варіантів варіантів
            arrays_list[count] = arr[num:num+length+1]
            count += 1
    count = 0
    for x in range(len(arrays_list)):
        if sum(arrays_list[x]) & 1:
            count += 1 

    return count

# list_to_calculate = [1,2,3,4]*100
list_to_calculate = [1, 2, 3, 4, 5, 6, 7]

print(solve(list_to_calculate))


# def solve(arr):
#     if len(arr) == 0:
#         return 0
#     arrays_list = []

# # перебор всіх можливих списків 
#     for length in range(len(arr)):  # length - довжина варіанту (1 символьний, 2 символьний і тд.)
        
#         for num in range(len(arr)-length):        # к-ть length-значних варіантів
#             array = [] # обнуляєм список з варіантом
#             for x in range(length+1):
#                 array.append(arr[num+x])  # додаєм варіант в список
#             if sum(array) % 2:
#                 arrays_list.append(array)     # додаєм список в список масивів перевіряючи умову Odd

#     return len(arrays_list)