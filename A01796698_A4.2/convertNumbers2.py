"""
Module to convert numbers from a file to Binary and Hexadecimal.
"""

# pylint: disable=invalid-name

import sys
import time


def to_binary(n):
    """Converts a number to binary using basic algorithms."""
    if n == 0:
        return "0"
    is_neg = n < 0
    n = int(abs(n))
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return "-" + res if is_neg else res


def to_hexadecimal(n):
    """Converts a number to hexadecimal using basic algorithms."""
    if n == 0:
        return "0"
    chars = "0123456789ABCDEF"
    is_neg = n < 0
    n = int(abs(n))
    res = ""
    while n > 0:
        res = chars[n % 16] + res
        n //= 16
    return "-" + res if is_neg else res


def process_file(file_path):
    """Reads file and returns a list of results."""
    data_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                val = line.strip()
                if not val:
                    continue
                try:
                    num = int(float(val))
                    data_list.append((num, to_binary(num), to_hexadecimal(num)))
                except ValueError:
                    print(f"Error: Invalid data '{val}' at line {i}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return data_list


def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        return

    start = time.time()
    results = process_file(sys.argv[1])
    elapsed = time.time() - start

    output = f"{'Number':<10} | {'Binary':<20} | {'Hexadecimal':<15}\n"
    output += "-" * 55 + "\n"
    for r in results:
        output += f"{r[0]:<10} | {r[1]:<20} | {r[2]:<15}\n"
    output += f"\nExecution Time: {elapsed:.6f} seconds\n"

    print(output)
    with open("ConvertionResults.txt", "w", encoding='utf-8') as f:
        f.write(output)


if __name__ == "__main__":
    main()