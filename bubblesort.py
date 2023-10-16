def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


input_array = input("Enter the array of integers (space-separated): ")
given_array = list(map(int, input_array.split()))


sorted_array = bubble_sort(given_array)


print("Sorted Array:", sorted_array)
