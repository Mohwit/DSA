array = [2, 4, 6, 9, 11, 12, 14, 20, 25, 30, 50, 60, 70, 80, 90, 100]

from typing import List

def binary_search(arr:List[int], target:int) -> int:
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        middle = (start + (end - start)) // 2
        
        if target < arr[middle]:
            end = middle - 1
            
        elif target > arr[middle]:
            start = middle + 1
        
        else:
            return middle
    
    return -1

print(binary_search(array, 11)) # 4