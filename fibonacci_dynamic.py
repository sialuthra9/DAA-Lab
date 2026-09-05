n = int(input("Enter the number of terms: "))

fib = [0] * n

if n > 0:
    fib[0] = 0

if n > 1:
    fib[1] = 1

for i in range(2, n):
    fib[i] = fib[i - 1] + fib[i - 2]

print("Fibonacci Series:")

for i in range(n):
    print(fib[i], end=" ")
