"""
On day 0 N different people sit in N different seats
both numbered from 0 to N-1. Each in their corresponding seat

There is a seat swapping list P of length N.
That contains all numbers from 0 to N-1

Every day people change their seats according to the seat
swapping list. Person at seat 'i' will go to the seat at P[i].

Given a seat swapping list and the number of days
compute the final configuration.

example:

seat_swap([0, 4, 3, 1, 2], 2)

Day 0: 0 1 2 3 4
Day 1: 0 3 4 2 1
Day 2: 0 2 1 4 3

Answer: [0,2,1,4,3]
"""

def seat_swap(swap_list: list[int], days: int) -> list[int]:
    # code goes here
    return swap_list


