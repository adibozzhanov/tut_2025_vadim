

# task 1
# given a list, return all possible permutations of a list
def perms(nums: list[int]) -> list[list[int]]:
    if len(nums) <= 1:
        return [nums]
    result = set()
    for i in range(len(nums)):
        rest = nums[:i] + nums[i + 1:]
        for p in perms(rest):
            result.add(tuple([nums[i]] + p))

    return [list(p) for p in result]

    
l = [1,2,3,4]


# task 2
# return all possible combinations of numbers from 0 to N of size K
def combos(n: int, k: int) -> list[list[int]]:
    def backtrack(current_num: int = 0, curr_list: list[int] = []):
        if len(curr_list) == k:
            res.append(curr_list.copy())
            return

        for i in range(current_num, n):
            curr_list.append(i)
            backtrack(i+1, curr_list)
            curr_list.pop()                          
    res = []  
    backtrack()

    return res
     
# task 3

# a * a  * (a * a)
# p = (a * a)
# res = p * p
def power(a, b, m):
    if b == 1:
        return a % m
    
    p = power(a, b // 2, m)
    
    if b % 2 == 0:
        return (p * p) % m
    
    return (p * p * a) % m


power(8951392, 75810938921090, 1000007)





