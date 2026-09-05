import time
import tracemalloc
import random
import matplotlib.pyplot as plt


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input sizes
input_sizes = [100, 500, 1000, 2000, 4000]

bubble_times = []
merge_times = []

bubble_memory = []
merge_memory = []


# Experimental analysis
for n in input_sizes:

    data = [random.randint(1, 10000) for _ in range(n)]

    # Bubble Sort
    arr = data.copy()

    tracemalloc.start()
    start_time = time.perf_counter()
bubble_sort(arr)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    bubble_times.append(end_time - start_time)
    bubble_memory.append(peak)


    # Merge Sort
    arr = data.copy()

    tracemalloc.start()
    start_time = time.perf_counter()

    merge_sort(arr)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    merge_times.append(end_time - start_time)
    merge_memory.append(peak)


# Display results
print("Input Size | Bubble Time | Merge Time | Bubble Memory | Merge Memory")

for i in range(len(input_sizes)):
    print(
        input_sizes[i],
        "|",
        bubble_times[i],
        "|",
        merge_times[i],
        "|",
       bubble_memory[i],
        "|",
        merge_memory[i]
    )


# Execution time graph
plt.plot(input_sizes, bubble_times, marker='o', label='Bubble Sort')
plt.plot(input_sizes, merge_times, marker='o', label='Merge Sort')

plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time Comparison")
plt.legend()
plt.show()


# Memory usage graph
plt.plot(input_sizes, bubble_memory, marker='o', label='Bubble Sort')
plt.plot(input_sizes, merge_memory, marker='o', label='Merge Sort')

plt.xlabel("Input Size")
plt.ylabel("Memory Usage (bytes)")
plt.title("Memory Usage Comparison")
plt.legend()
plt.show()
