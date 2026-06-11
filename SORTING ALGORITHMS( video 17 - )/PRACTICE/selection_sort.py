def selectionSort(a):
    min = 0
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i + 1 , n):
            if(a[min] > a[j]):
                min = j
        a[min] , a[i] = a[i] , a[min]

a = [32 , 64 , 4 , 2]
selectionSort(a)
print(a)
