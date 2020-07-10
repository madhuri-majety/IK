"""
Selection sort to select min element at every pass and store it at the beginning
"""

def seletion_sort(arr):
    for i in range(len(arr)-1):
        imin = i
        for j in range(i+1, len(arr)):
            if arr[j] <= arr[imin]:
                imin = j

        arr[i],arr[imin] = arr[imin],arr[i]



x = [4,2,5,1,2,6,7]
seletion_sort(x)
print(x)
