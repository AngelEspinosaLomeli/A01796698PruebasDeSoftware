"""
Program to compute descriptive statistics from a file.
"""

import sys
import time


def get_numbers_from_file(file_path):
    """Reads a file and returns a list of valid numbers."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                clean_line = line.strip()
                if not clean_line:
                    continue
                try:
                    numbers.append(float(clean_line))
                except ValueError:
                    print(f"Error: Invalid data '{clean_line}' at line {line_num}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return numbers


def compute_statistics(data):
    """Calculates mean, median, mode, variance, and std deviation."""
    n = len(data)
    if n == 0:
        return None

    # Mean
    total_sum = 0
    for x in data:
        total_sum += x
    mean = total_sum / n

    # Median
    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    # Mode
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    
    max_count = 0
    for count in counts.values():
        if count > max_count:
            max_count = count
    
    modes = [val for val, count in counts.items() if count == max_count]
    mode = modes[0] if len(modes) == 1 else modes

    # Variance (Sample)
    sum_sq_diff = 0
    for x in data:
        sum_sq_diff += (x - mean) ** 2
    variance = sum_sq_diff / (n - 1) if n > 1 else 0

    # Standard Deviation
    std_dev = variance ** 0.5

    return {
        "Count": n,
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Variance": variance,
        "Std Dev": std_dev
    }


def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]
    
    data = get_numbers_from_file(file_path)
    stats = compute_statistics(data)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    if stats:
        output = (
            f"{'Statistic':<15} | {'Value':<15}\n"
            f"{'-' * 33}\n"
            f"{'Count':<15} | {stats['Count']:<15.2f}\n"
            f"{'Mean':<15} | {stats['Mean']:<15.4f}\n"
            f"{'Median':<15} | {stats['Median']:<15.4f}\n"
            f"{'Mode':<15} | {str(stats['Mode']):<15}\n"
            f"{'Variance':<15} | {stats['Variance']:<15.4f}\n"
            f"{'Std Dev':<15} | {stats['Std Dev']:<15.4f}\n"
            f"{'Time Elapsed':<15} | {elapsed_time:<15.6f} s\n"
        )

        print(output)

        with open("StatisticsResults.txt", "w", encoding='utf-8') as f:
            f.write(output)


if __name__ == "__main__":
    main()