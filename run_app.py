# run_app.py

import os
import datetime

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def write_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def main():
    # Get current date
    current_date = datetime.datetime.now()
    
    # Create results subfolder if it doesn't exist
    results_folder = "results"
    os.makedirs(results_folder, exist_ok=True)

    # Generate Fibonacci sequence
    n = 10  # You can adjust the value of 'n' based on how many Fibonacci numbers you want
    fib_result = fibonacci(n)

    # Create a filename based on the current date
    filename = f"{results_folder}/{current_date.year}_{current_date.month:02d}_{current_date.day:02d}_results.txt"

    # Write Fibonacci sequence to the file
    write_to_file(fib_result, filename)

    print(f"Fibonacci sequence written to {filename}")

if __name__ == "__main__":
    main()
