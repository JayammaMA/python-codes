# Function to generate Fibonacci sequence up to 'n' terms
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence

# Example usage
n = int(input("Enter the number of terms: "))
result = fibonacci(n)
print(f"Fibonacci sequence with {n} terms: {result}")
