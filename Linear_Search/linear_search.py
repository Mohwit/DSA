from typing import List


## Linear Search
def linearSearch(arr: List, target: int) -> int:
    ## checking for an empty array
    if len(arr) == 0:
        return -1

    ## looping through the array
    for index in range(len(arr)):
        if arr[index] == target:
            return index

    ## if no element is found
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5
    print(linearSearch(arr, target))
