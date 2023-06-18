import numpy as np

# Insertion Sort (Ekleme Sıralaması)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Selection Sort (Seçmeli Sıralama)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Merge Sort (Birleştirme Sıralaması)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# Bubble Sort (Kabarcık Sıralaması)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ana kod
arr = np.array([64, 34, 25, 12, 22, 11, 90])
print("Veri Dizisi:", arr)

sorted_arr = insertion_sort(arr.copy())
print("Insertion Sort ile Sıralama:", sorted_arr)

sorted_arr = selection_sort(arr.copy())
print("Selection Sort ile Sıralama:", sorted_arr)

sorted_arr = merge_sort(arr.copy())
print("Merge Sort ile Sıralama:", sorted_arr)

sorted_arr = bubble_sort(arr.copy())
print("Bubble Sort ile Sıralama:", sorted_arr)

print("***************************************************")

import numpy as np
a = np.array([34, 5, 89, 23, 76])
print(np.sort(a))

def sorting(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
print(sorting(a))