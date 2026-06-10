
def bubbleSort(arr):
    n = len(arr)
    for j in range(0,n - 2): # last element is excluded
        for i in range(0,n - j - 1):
         if(arr[i] > arr[i + 1]):
            arr[i], arr[i + 1] =  arr[i + 1], arr[i]


arr = [12 , 3 ,4, 90 , 78 , 23 , 64]
bubbleSort(arr)
print(arr)

# n = len(arr)
# for k in range(n):
#     print(arr[k] , end = " ")

# TIME COMPLEXITY = O(n2)
