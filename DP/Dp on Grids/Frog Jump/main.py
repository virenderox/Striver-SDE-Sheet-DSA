def frogJump(N,height):

    return solve(N-1,height,{})

def solve(current,height,dic):

    if current == 0:
        return 0

    if current in dic:
        return dic[current]

    jumpOne = solve(current - 1,height,dic) + abs(height[current] - height[current-1])
    jumpTwo = float("inf")
    
    if current > 1:
        jumpTwo = solve(current - 2,height,dic) + abs(height[current] - height[current-2])

    dic[current] = min(jumpOne,jumpTwo)
    return dic[current]

