import matplotlib.pyplot as plt

# Input sizes
input_sizes = [100, 500, 1000, 2000, 4000]

# Experimental results
bubble_times = [0.0003384, 0.0542740, 0.4939032, 2.3319095, 12.4342941]
merge_times = [0.0002723, 0.0014103, 0.0083891, 0.0113759, 0.0454848]

bubble_memory = [184, 260, 1084, 292, 1116]
merge_memory = [1992, 8480, 17272, 34160, 66320]


# Execution Time Graph
plt.plot(input_sizes, bubble_times, marker='o', label='Bubble Sort')
plt.plot(input_sizes, merge_times, marker='o', label='Merge Sort')

plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time Comparison")
plt.legend()
plt.show()


# Memory Usage Graph
plt.plot(input_sizes, bubble_memory, marker='o', label='Bubble Sort')
plt.plot(input_sizes, merge_memory, marker='o', label='Merge Sort')

plt.xlabel("Input Size")
plt.ylabel("Memory Usage (bytes)")
plt.title("Memory Usage Comparison")
plt.legend()
plt.show()
