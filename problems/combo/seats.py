import random
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
#          0  1  2  3  4
seat_swap([0, 4, 3, 1, 2], 2)
           0  3  e  c  4

a = [0, 4, 3, 1, 2]
days = 4

Day 0: 0 1 2 3 4
Day 1: 0 3 4 2 1
Day 2: 0 2 1 4 3
Day 3: 0 4 3 1 2
Day 4: 0 1 2 3 4

[0, 4, 3, 1, 2] * [0, 4, 3, 1, 2] = r
r * [0, 4, 3, 1, 2] =  0 3 4 2 1

0 1 2 3 4
1 2 3 4 0


Answer: [0,2,1,4,3]
perm1 = 0 1 2 3 4
perm2 = 0 4 3 1 2
perm3 = 0 3 4 2 1

commutative
identity_element
zero_element
inverse


multiply(perm1,  perm2) -> perm3
"""

def perm(l1: list[int], p: list[int]) -> list[int]:
    l2 = [0 for _ in l1]
    
    for i in range(len(l1)):
        l2[p[i]] = l1[i]
        
    return l2

def identity(n):
    return list(range(n))



arr = list(range(1000000))
random.shuffle(arr)

def seat_swap(a: list[int], b: int) -> list[int]:    
    current = identity(len(a))
    if b == 1:
        return a
    p = seat_swap(a, b //2)
    
    if b % 2 == 0:
        return perm(p,p)
    
    return perm(perm(p,p),a)

days = 2
l = [0, 4, 3, 1, 2]
print(seat_swap(l, days))


