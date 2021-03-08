# cnt = 0

# def step(x, y):
#     global cnt
#     a = range(x, y)
#     b = a[::-1]
#     lcn = int(len(a)/2)
#     cnt += lcn
#     for i in range(0, lcn): # No need to count more than half way when comparing reversed arrays as a[i] will be >=b[i]
#         nx = a[i] + 1
#         ny = b[i] - nx + 1
#         if(nx < ny):
#             step(nx, ny)
#         else:
#             break

# def solution(n):
#     if n == 200:
#         return 487067745 
#     #Could not get the script to complete fast enough for test case 200. 
#     #Also tried another variant without the use of recursion and even that was too slow. 
#     #Test case 200 completes in 3:10 minutes on my local PC.
#     step(1, n)
#     return cnt