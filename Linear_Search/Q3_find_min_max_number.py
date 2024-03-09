""" Question 3: Find the minimum and maximum number """

from typing import List


## function to find the minimum number in an array
def minimum(arr: List) -> int:
    ## checking for an empty array
    if len(arr) == 0:
        return -1

    ## setting the minimum to the first element
    min = arr[0]

    ## looping through the array
    for index in range(len(arr)):
        if arr[index] < min:
            min = arr[index]

    return min


## function to find the maximum number in an array
def maximum(arr: List) -> int:
    ## checking for an empty array
    if len(arr) == 0:
        return -1

    ## setting the maximum to the first element
    max = arr[0]

    ## looping through the array
    for index in range(len(arr)):
        if arr[index] > max:
            max = arr[index]

    return max


## function to find the minimum in a 2-d array
## returns the index of the minimum
def minimum_2d(arr: List[List[int]]) -> List[int]:
    ## checking for an empty array
    if len(arr) == 0:
        return -1

    ## setting the minimum to the first element
    min = arr[0][0]

    ## looping through the array
    ## looping through the rows
    for row in range(len(arr)):
        ## looping through the columns
        for column in range(len(arr[row])):
            if arr[row][column] < min:
                min = arr[row][column]
                index = [row, column]

    ## returning the index of the minimum
    return index


## function to find the maximum in a 2-d array
## returns the index of the maximum
def maximum_2d(arr: List[List[int]]) -> List[int]:
    ## checking for an empty array
    if len(arr) == 0:
        return -1

    ## setting the maximum to the first element
    max = arr[0][0]

    ## looping through the array
    ## looping through the rows
    for row in range(len(arr)):
        ## looping through the columns
        for column in range(len(arr[row])):
            if arr[row][column] > max:
                max = arr[row][column]
                index = [row, column]

    ## returning the index of the maximum
    return index


## testing the functions
if __name__ == "__main__":
    arr = [18, 12, -7, 3, 14, 28]
    arr_2d = [[18, 12, -7], [3, 14, 28]]
    print(minimum(arr))
    print(maximum(arr))
    print(minimum_2d(arr_2d))
    print(maximum_2d(arr_2d))
