def insertion_sort(list_to_sort):
    # Separate the first element from the rest of the array. Think about it as a sorted list of one element.
​
    # For all other indices, beginning with [1]:
    for i in range(1, len(list_to_sort)):
​
        # a. Copy the item at that index into a temp variable
        temp = list_to_sort[i]
​
        # b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        j = i
        while j > 0 and temp < list_to_sort[j-1]:
            print(j)
            # Shift items over to the right as you iterate
            list_to_sort[j] = list_to_sort[j - 1]
            j -= 1
        # c. When the correct index is found, copy temp into this position
        list_to_sort[j] = temp
​
    return list_to_sort


# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j



        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]




    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort( arr ):
    # loop through the whole array not including the first index
    for i in range(1, len(arr)):
        # loop through the array including the first index.
        for j in range(0, len(arr) - 1):
            # compare current index to the index right beside it -- or to the right of it.
            if arr[j] > arr[j + 1]:
                # swap them.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr