# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    a = 0
    b = 0

    while a < len(arrA) and b < len(arrB):
        # combine the elements that a and b point at
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    # at this point, we'be traversed one of the lists
    # we need to add all of the elements of from the other list to the merged_arr
    while a < len(arrA):
        merged_arr.append(arrA[a])
        a += 1
    while b < len(arrB):
        merged_arr.append(arrB[b])
        b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Break the array down recursively
    # base case: when the lists get down to 1

    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    # then merge them back up    

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
