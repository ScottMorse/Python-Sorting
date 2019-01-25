# O(n^2)
def bubble_sort(arr):
    was_swap = False

    for i in range(len(arr)):
        if i == 0:
            continue
        if arr[i] < arr[i - 1]:
            prev = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = prev
            was_swap = True
    
    if was_swap:
        arr = bubble_sort(arr)

    return arr

# O(n^2)
def selection_sort(arr):
    for slice_i in range(len(arr)):
        current_min = arr[slice_i]
        min_index = slice_i
        for i in range(slice_i + 1,len(arr)):
            if arr[i] < current_min:
                current_min = arr[i]
                min_index = i
        prev = arr[slice_i]
        arr[slice_i] = current_min
        arr[min_index] = prev
    return arr

#O(n^2)
def insertion_sort(arr):
    if(len(arr) < 2):
        return arr
    if(len(arr) == 2):
        return arr if arr[0] < arr[1] else [arr[1],arr[0]]
    for slice_i in range(1,len(arr)):
        for i in range(slice_i,0,-1):
            if arr[i] < arr[i - 1]:
                prev = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = prev
            else:
                break
    return arr

from random import randint

def quick_sort_bad(arr):
    random_index = randint(0,len(arr) - 1)

    pivot = arr[random_index]

    left_arr = []
    right_arr = []

    for item in arr[:random_index] + (arr[random_index + 1:] if random_index < len(arr) - 1 else []):
        if item < pivot:
            left_arr.append(item)
        else:
            right_arr.append(item)
    
    if len(left_arr) > 0:
        left_arr = quick_sort(left_arr)

    if len(right_arr) > 0:
        right_arr = quick_sort(right_arr)
    
    return left_arr + [pivot] + right_arr

#in place
def quick_sort(arr): 
    if len(arr) < 2:
        return

    def partition(arr,low,high): 
        pivot = arr[high]
        i = low
    
        for j in range(low, high): 
            if arr[j] <= pivot: 
                arr[i], arr[j] = arr[j], arr[i] 
                i += 1

        arr[i], arr[high] = arr[high], arr[i] 
        return i

    def _quick_sort(arr,low=0,high=None):
        if high == None:
            high = len(arr) - 1
        if low < high: 
            pi = partition(arr,low,high) #partition index
            _quick_sort(arr, low, pi-1) 
            _quick_sort(arr, pi+1, high) 

    _quick_sort(arr)

def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0 # left pointer at subarray
        j = 0 # right pointer at subarray
        k = 0 # in place for array

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i += 1
            else:
                alist[k]=righthalf[j]
                j += 1
            k += 1

        #add missing tails to end
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j += 1
            k += 1