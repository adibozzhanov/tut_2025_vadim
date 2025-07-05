from functools import cache

def rule(pebble: str) -> list[str]:
    if pebble =="0":
        return ["1"]

    if len(pebble) % 2 == 0:
        return [
            str(int(pebble[:len(pebble)//2])), 
            str(int(pebble[len(pebble)//2:]))
        ]

    return [str(int(pebble) * 2024)]

def blink(pebbles: list) -> list:
    ret = []
    for pebble in pebbles:
        new_pebbles = rule(pebble)
        ret.extend(new_pebbles)        
    return ret
    

def sol():
    current = input().split()
    for i in range(75): # 
        current = blink(current)
    print(len(current))

@cache
def solve(pebble: str, blink: int) -> int:
    if blink == 0:
        return 1
    return sum([solve(p, blink-1) for p in rule(pebble)])




vals = input().split()



print(
    sum([
        solve(val, 75) for val in vals
    ])
)

    
    
    
    
    
    



    



