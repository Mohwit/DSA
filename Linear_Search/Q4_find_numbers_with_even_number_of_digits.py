"""Question 4: Find number of numbers with even number of digits"""

from typing import List


## function to find the number of numbers with even number of digits
## Method 1:
def findNumber(nums: List[int]) -> int:
    count = 0

    ## looping through the array
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count


## Method 2:


## function to check if the number of digits is even or not
def even(num: int) -> bool:
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count % 2 == 0


## function to find the number of numbers with even number of digits
def findNumber2(nums: List[int]) -> int:
    count = 0

    ## looping through the array
    for num in nums:
        ## checking for the number of digits is even or not
        if even(num):
            count += 1

    return count


## testing the function
if __name__ == "__main__":
    nums = [12, 345, 2, 6, 7896]
    print(findNumber(nums))
    nums = [555, 901, 482, 1771]
    print(findNumber(nums))
    nums = [10000]
    print(findNumber(nums))
