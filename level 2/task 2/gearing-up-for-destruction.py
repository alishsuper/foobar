def solution(pegs):
    # Your code here
    temp_sum = 2*(sum(pegs[1::2]) - sum(pegs[::2])) + pegs[0]
    if len(pegs) % 2 == 0:
        r_a = 2* (temp_sum - pegs[-1])
        r_b = 3
        if (r_a % r_b) == 0:
            r_a = r_a // r_b
            r_b = 1
    else:
        r_a = 2 * (temp_sum + pegs[-1])
        r_b = 1
        
    last_gear = r_a / r_b
    for i in range(len(pegs) - 1):
        last_gear = pegs[i+1] - pegs[i] - last_gear
        if last_gear < 1:
            return [-1, -1]
            
    result = []
    result.append(r_a)
    result.append(r_b)
    return result