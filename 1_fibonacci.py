import time

# -------- Recursive Fibonacci --------
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# -------- Non-Recursive Fibonacci --------
def fib_non_recursive(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# -------- Main --------
def main():
    n = int(input("Enter the number of elements: "))

    # Recursive output
    print("\nFibonacci (Recursive): ", end="")
    start = time.time()
    for i in range(n):
        print(fib_recursive(i), end=" ")
    rec_time = (time.time() - start) * 1_000_000

    # Non-recursive output
    print("\n\nFibonacci (Non-Recursive): ", end="")
    start = time.time()
    seq = fib_non_recursive(n)
    print(*seq)
    nonrec_time = (time.time() - start) * 1_000_000

    # -------- Complexity --------
    print("\n=== Time and Space Complexity ===")
    print(f"Recursive Time Taken: {rec_time:.2f} microseconds")
    print("Recursive Time Complexity: O(2^n)")
    print("Recursive Space Complexity: O(n)\n")

    print(f"Non-Recursive Time Taken: {nonrec_time:.2f} microseconds")
    print("Non-Recursive Time Complexity: O(n)")
    print("Non-Recursive Space Complexity: O(1)")

if __name__ == "__main__":
    main()
