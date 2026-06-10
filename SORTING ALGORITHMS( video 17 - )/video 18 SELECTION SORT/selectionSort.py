def selectionSort(a):
    n = len(a)
    min = 0

    for i in range(n):
        min = i
        for j in range(i+1,n):
            if(a[min] > a[j]):
                min = j
        a[i] , a[min] = a[min] , a[i]

# SELECT min value index and swap them.

a = [12 , 4 , 2 , 45 , 88 , 900]

selectionSort(a)

print(a)

# time complexity = O(n2)
