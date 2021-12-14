from random import randint
import timeit
import time
import sys
import matplotlib.pyplot as plt
sys.setrecursionlimit(5000)
Input_sizes= [1000,2000,4000,5000,10000,20000,30000,40000,50000]
j=1
rand_array= []
Final_array=[]
Sorted_array=[]
Reverse_array=[]
for i in range(len(Input_sizes)):
    j=1
    while j <= Input_sizes[i]:
        rand_array.append(randint(0, 1000))
        j = j+ 1
    Final_array.append(rand_array)
    Sorted_array.append(sorted(rand_array))
    Reverse_array.append(sorted(rand_array,reverse=True))
    rand_array = []

###################### Insertion Sort ###############################
def Insertion_Sort(arr):
        excecution_time = []
        for i in range(len(arr)):
            start_time = time.time()
            for k in range(len(arr[i])):
                key = arr[i][k]
                j = k - 1
                while j >= 0 and key < arr[i][j]:
                    arr[i][j + 1] = arr[i][j]
                    j = j - 1
                    arr[i][j + 1] = key
            end_time = time.time()
            excecution_time.append(end_time - start_time)
        print("InsertionSort Random case")
        print("--------------------------")
        for i in range(len(arr)):
            print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))
        return arr
Insertion_Sort(Final_array)
# Sorted array
def Sorted_Insert_Sort(arr):
    excecution_time = []
    for i in range(len(arr)):
        start_time = time.time()
        for k in range(len(arr[i])):
            key = arr[i][k]
            j = k - 1
            while j >= 0 and key < arr[i][j]:
                arr[i][j + 1] = arr[i][j]
                j = j - 1
                arr[i][j + 1] = key
        end_time = time.time()
        excecution_time.append(end_time - start_time)
    print("InsertionSort Sorted Case")
    print("--------------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))


Sorted_Insert_Sort(Sorted_array)

# Reversly Sorted array
def ReverslySorted_insert_Sort(arr):
    excecution_time = []
    for i in range(len(arr)):
        start_time = time.time()
        for k in range(len(arr[i])):
            key = arr[i][k]
            j = k - 1
            while j >= 0 and key < arr[i][j]:
                arr[i][j + 1] = arr[i][j]
                j = j - 1
                arr[i][j + 1] = key
        end_time = time.time()
        excecution_time.append(end_time - start_time)
    print("InsertionSort Reversly Sorted Case")
    print("------------------------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))

ReverslySorted_insert_Sort(Reverse_array)
############################### Merge Sort ###################################
def merge_perform(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves
        merge_perform(L)  # Sorting the first half
        merge_perform(R)  # Sorting the second half
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
#random main function
def Merge_Sort(arr):
        excecution_time = []
        OutPut_array = []
        for i in range(len(arr)):
            start_time = time.time()
            OutPut_array.append(merge_perform(arr[i]))
            end_time = time.time()
            excecution_time.append(end_time - start_time)
        print("MergeSort Random case:")
        print("-----------------------")
        for i in range(len(arr)):
            print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))

        return OutPut_array

#increasing order main function
def Sorted_merge_Sort(arr):
        excecution_time = []
        OutPut_array = []
        for i in range(len(arr)):
            start_time = time.time()
            OutPut_array.append(merge_perform(arr[i]))
            end_time = time.time()
            excecution_time.append(end_time - start_time)
        print("MergeSort Sorted case:")
        print("--------------------")
        for i in range(len(arr)):
            print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))
        return OutPut_array


#decreasing order main function
def Reverslysorted_merge_Sort(arr):
        excecution_time = []
        OutPut_array = []
        for i in range(len(arr)):
            start_time = time.time()
            OutPut_array.append(merge_perform(arr[i]))
            end_time = time.time()
            excecution_time.append(end_time - start_time)
        print("MergeSort Reversly Sorted case:")
        print("---------------------------------")
        for i in range(len(arr)):
            print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))
        return OutPut_array

#calling functions
Merge_Sort(Final_array)
Sorted_merge_Sort(Sorted_array)
Reverslysorted_merge_Sort(Reverse_array)
################################# Heap Sort #################################################
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)

def heapPerform(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

def heapSort(arr):
    excecution_time = []
    for i in range(len(arr)):
        start_time = time.time()
        heapPerform(arr[i])
        end_time = time.time()
        excecution_time.append(end_time - start_time)
    print("HeapSort Random case:")
    print("---------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))

    return arr, excecution_time

def Sorted_heapSort(arr):
    excecution_time = []
    for i in range(len(arr)):
        start_time = time.time()
        heapPerform(arr[i])
        end_time = time.time()
        excecution_time.append(end_time - start_time)
    print("HeapSort Sorted case:")
    print("-------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))

    return arr, excecution_time

def Reverslysorted_heapSort(arr):
    excecution_time = []
    for i in range(len(arr)):
        start_time = time.time()
        heapPerform(arr[i])
        end_time = time.time()
        excecution_time.append(end_time - start_time)
    print("HeapSort Reversly Sorted case:")
    print("-------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))

    return arr, excecution_time


heapSort(Final_array)
Sorted_heapSort(Sorted_array)
Reverslysorted_heapSort(Reverse_array)

#################################### InPlace QuickSort ########################################

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def Inplacequick_Sort(arr):
    excecution_time = []
    for i in range(len(arr)):
            start_time = time.time()
            n = len(arr[i])
            quickSort(arr[i], 0, n - 1)
            end_time = time.time()
            excecution_time.append(end_time - start_time)
    print("InPlaceQuickSort Random case:")
    print("----------------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))
    return arr

def Sorted_Inplacequick_Sort(arr):
    excecution_time = []
    for i in range(len(arr)):
            start_time = time.time()
            n = len(arr[i])
            quickSort(arr[i], 0, n - 1)
            end_time = time.time()
            excecution_time.append(end_time - start_time)
    print("InPlaceQuickSort Sorted case:")
    print("---------------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))
    return arr

def decreasing_inplacequick_Sort(arr):
    excecution_time = []
    for i in range(len(arr)):
            start_time = time.time()
            n = len(arr[i])
            quickSort(arr[i], 0, n - 1)
            end_time = time.time()
            excecution_time.append(end_time - start_time)
    print("InPlaceQuickSort Reversly Sorted case:")
    print("------------------------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))
    return arr

Inplacequick_Sort(Final_array)
Sorted_Inplacequick_Sort(Sorted_array)
decreasing_inplacequick_Sort(Reverse_array)

############################## Modified Quicksort (median of three)######################################
mediancomp=0
def insertionsort(arr,left,right):
    for k in range(1, len(arr)):
        key = arr[k]
        j = k - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    return arr

def median(a, b, c):
    if (a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c

# A method to partition around the median
def partition_median(array, leftend, rightend):
    left = int(array[leftend])
    right = int(array[rightend - 1])
    length = int(rightend - leftend)
    if length % 2 == 0:
        middle = array[int(leftend + (length / 2) - 1)]
    else:
        middle = array[int(leftend + length / 2)]

    pivot = median(left, right, middle)

    pivotindex = array.index(pivot)
    array[pivotindex] = array[leftend]
    array[leftend] = pivot

    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i - 1]
    array[i - 1] = leftendval
    return i - 1

def QuickSort(arr,low,high):
    if low < high:
            newpivotindex = partition_median(arr, low, high)
            mediancomp = int((high - low - 1)) + 1
            QuickSort(arr, low, newpivotindex)
            QuickSort(arr, newpivotindex + 1, high)

def medianQuickSort(array, LIndex, RIndex):
    global mediancomp
    compare = int(RIndex-LIndex)
    if LIndex >= RIndex:
        return
    elif compare <= 15:
        insertionsort(array, LIndex, RIndex)
    elif LIndex < RIndex:
            # newpivotindex = partition_median(array, LIndex, RIndex)
            # mediancomp = int((RIndex - LIndex - 1)) + 1
            QuickSort(array, LIndex, RIndex)


def Modifiedquick_Sort(arr):
    excecution_time = []
    for i in range(len(arr)):
            start_time = time.time()
            medianQuickSort(arr[i], 0, len(arr[i]))
            end_time = time.time()
            excecution_time.append(end_time - start_time)
    print("ModifiedQuickSort Random case:")
    print("------------------------------------")

    for i in range(len(arr)):
            print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))

    return arr

def Sorted_Modifiedquick_Sort(arr):
    excecution_time = []
    for i in range(len(arr)):
            start_time = time.time()
            medianQuickSort(arr[i], 0, len(arr[i]))
            end_time = time.time()
            excecution_time.append(end_time - start_time)
    print("ModifiedQuickSort Sorted case:")
    print("------------------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))
    return arr

def ReverslySorted_modifiedquick_Sort(arr):
    excecution_time = []
    for i in range(len(arr)):
            start_time = time.time()
            medianQuickSort(arr[i], 0, len(arr[i]))
            end_time = time.time()
            excecution_time.append(end_time - start_time)
    print("ModifiedQuickSort Reversly Sorted case:")
    print("------------------------------------")
    for i in range(len(arr)):
        print("Sorting of " + str(len(arr[i])) + " elements runs in " + str(excecution_time[i]))
    return arr

Modifiedquick_Sort(Final_array)
Sorted_Modifiedquick_Sort(Sorted_array)
ReverslySorted_modifiedquick_Sort(Reverse_array)
