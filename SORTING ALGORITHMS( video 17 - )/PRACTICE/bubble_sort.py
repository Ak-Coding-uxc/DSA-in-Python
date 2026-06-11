def bubbleSort(a):
    n = len(a)
    for i in range(0,n-1):
        for j in range(0,n - i - 1):
            if(a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1] , a[j]

a = [32 , 64 , 4 , 2]
bubbleSort(a)
print(a)