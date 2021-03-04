def solution(l, t):
    # Your code here

    left = 0
    right = 0
    while right < len(l):
        sum_s = 0
        for i in range(left, right + 1):
            sum_s = sum_s + l[i]

        if sum_s == t:
            print(left, right)
            return left, right
        elif sum_s < t:
            right += 1
        elif sum_s > t:
            left += 1
            if left > right:
                right += 1
    print([-1, -1])
solution([12], 12)