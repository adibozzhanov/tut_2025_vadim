CASE = "pyramid_1.txt"

def solve(pyr: list[list[int]]) -> int:
    # find minimum path sum
    print("\n".join([str(x) for x in pyr]))
    
    return 1

with open(CASE, "r") as f:
    lines = f.readlines()
    pyramid = [[ int(i) for i in l.split()] for l in lines]
    print(solve(pyramid))


