def maxSubArray(arr):
    maxSum = 0
    curSum = 0
    for i in range(len(arr)):
        curSum = curSum + arr[i]
        if(curSum > maxSum):
            maxSum = curSum
        if(curSum<0):
            curSum = 0
    return maxSum


arr=[-25,-12,66,-15,-34,15,76,45,2,-22,-43,-26,65,-34,22,14,-51,56,44,9]
print(f"Input array: {arr}")
print(f"Maximum sum is: {maxSubArray(arr)}")
