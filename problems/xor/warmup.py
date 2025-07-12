import random
# XOR operator in python
a = 15 
b = 13 

print("{:04b}".format(a))
print("{:04b}".format(b))
print("{:04b}".format(a ^ b))

# Task 1: swap 2 variables
# rules:
# - You cannot create new variables
# - You cannot use inline multiple assignment syntax i.e. a,b = 13, 15
# - You have to use XOR in some way

_a, _b = random.randint(0,1000), random.randint(0,1000)
a, b = _a, _b
print(f"BEFORE: {a}, {b}")
# v CODE GOES HERE v
# ==================

# =================
print(f"AFTER: {a}, {b}")
assert a == _b
assert b == _a


