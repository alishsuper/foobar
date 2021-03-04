
def solution(area):
    result = []

    def recursion(area):
        if area == 0:
            return
        if area < 2:
            result.append(1)
            return
        
        x = area // 2
        while x * x > area:
            x = (x + area // x) // 2
        result.append(x * x)
        recursion(area - (x * x))
    recursion(area)
    print(result)
solution(16)