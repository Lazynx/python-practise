def solve(numheads, numlegs):
    x = numlegs - numheads * 2
    return f"Chickens: {x / 2} Rabbits: {numheads - x / 2}"


print(solve(35, 94))
