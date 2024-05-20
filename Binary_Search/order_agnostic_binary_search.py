from typing import List

array = [2, 4, 6, 9, 11, 12, 14, 20, 25, 30, 50, 60, 70, 80, 90, 100]

def order_agnostic_binary_search(array:List[int], target:int) -> int:
    start = 0
    end = len(array) - 1

    ## finding if array is sorted in ascending or descending
    is_ascending: bool = array[start] - array[end]

    while start <= end:
        middle = start + (end-start) // 2

        if array[middle] == target:
            return middle

        ## if order is ascending
        if (is_ascending):
            if(target < array[middle]):
                end = middle - 1
            
            else:
                start = middle + 1

        ## if array is descending 
        else:
            if(target > array[middle]):
                end = middle - 1
            
            else:
                start = middle + 1
    
    ## if target not found
    return -1


if __name__ == "__main__":
    print(order_agnostic_binary_search(array=array,target=100))
