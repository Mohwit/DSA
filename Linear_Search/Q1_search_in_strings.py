""" Question: Search in Strings """


## Function to search for a target in a string
def search(string: str, target: str) -> int:
    ## checking for an empty string
    if len(string) == 0:
        return -1

    ## looping through the string
    for index in range(len(string)):
        if string[index] == target:
            return index

    ## if no element is found
    return -1


## testing the function
if __name__ == "__main__":
    string = "Hello, World!"
    target = "W"
    print(search(string, target))
