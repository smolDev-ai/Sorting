# def partition(data):
#     left = []
#     pivot = data[0]
#     right = []

#     for item in data[1:]:
#         if item < pivot:
#             left.append(item)
#         else: # Handling > or =
#             right.append(item)
# ​
#     return left, pivot, right
# ​
# def quicksort(data):
#     if data == []:
#         return data
    
#     left, pivot, right = partition(data)
# ​
#     return quicksort(left) + [pivot] + quicksort(right)
# ​
# print(quicksort(my_list))



# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    m = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] > arrB[b]:
            merged_arr[m] = arrB[b]
            b += 1
        elif arrA[a] < arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
        m += 1

    while a < len(arrA):
        merged_arr[m] = arrA[a]
        a += 1
        m += 1

    while b < len(arrB):
        merged_arr[m] = arrB[b]
        b += 1
        m += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if arr == [] or len(arr) < 2:
        return arr
    
    left = merge_sort(arr[len(arr) // 2:])
    right = merge_sort(arr[:len(arr) // 2])
    
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
