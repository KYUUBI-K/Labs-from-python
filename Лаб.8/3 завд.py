def x(n):
    arr = [0,9,9]
    for i in range(3,n+1):
        gt = arr[i-1]+4*arr[i-3]
        arr.append(gt)
    return arr[n]
i = int(input())
print(x(i))

