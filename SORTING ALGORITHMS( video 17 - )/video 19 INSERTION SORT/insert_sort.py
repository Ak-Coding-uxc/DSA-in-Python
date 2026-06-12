def insertionSort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i + 1 , 0, -1):
            if(a[j] < a[j - 1]):
                a[j],a[j - 1] = a[j -1 ] , a[j]


a = [12 , 34 , 4 ,5 ,1]
insertionSort(a)
print(a)


# time complexity = O(n2)