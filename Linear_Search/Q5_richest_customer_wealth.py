""" Question 5: You are given am m x n integer grid accounts where accounts[i][j] is the amount of money the i-th customer has in 
the j-th bank. Return the wealth that the richest customer has. A customer's wealth is the amount of money they have in all their 
bank accounts. The richest customer is the customer that has themaximum wealth"""

from typing import List

## function to find the wealth of the richest customer
def richest_customer_wealth(accounts: List[List[int]]) -> int:
    ## initialize the max_wealth to 0
    max_wealth = 0
    ## iterate through the accounts and find the sum of each customer's wealth
    for i in range(len(accounts)):
        max_wealth = max(max_wealth, sum(accounts[i]))
    return max_wealth

## using list comprehension
def richest_customer_wealth(accounts: List[List[int]]) -> int:
    return max([sum(accounts[i]) for i in range(len(accounts))])

## testing the function
if __name__ == '__main__':
    accounts = [[1,2,3],[3,2,1]]
    print(richest_customer_wealth(accounts)) # 6