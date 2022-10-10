def solution(arr):
    if len(arr)> 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]

x1 = [4,0,2,1]
print(solution(x1))