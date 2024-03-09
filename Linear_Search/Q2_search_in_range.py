"""
Question 2: Search in a given range
Given array: [18, 12, -7, 3, 14, 28]
Search for the target 3 in the range 1 to 4
"""

from typing import List


## Function to search for a target in a given range
def search_in_range(arr: List[int], target: int, start: int, end: int) -> int:
    ## checking for an empty array
    if len(arr) == 0:
        return -1

    ## looping through the array
    for index in range(start, end):
        if arr[index] == target:
            return index

    ## if no element is found
    return -1


## testing the function
if __name__ == "__main__":
    arr = [18, 12, -7, 3, 14, 28]
    target = 18
    start = 1
    end = 4
    print(search_in_range(arr, target, start, end))
