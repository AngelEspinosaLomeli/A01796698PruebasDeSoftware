"""
Módulo para convertir números de un archivo a binario y hexadecimal.
"""

# pylint: disable=invalid-name

import sys
import time


def to_binary(n):
    """Convierte un número a binario utilizando algoritmos básicos."""
    if n == 0:
        return "0"
    is_negative = n < 0
    n = int(abs(n))
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return "-" + binary if is_negative else binary


def to_hexadecimal(n):
    """Convierte un número a hexadecimal utilizando algoritmos básicos."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    is_negative = n < 0
    n = int(abs(n))
    hexadecimal = ""
    while n > 0:
        remainder = n % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        n //= 16
    return "-" + hexadecimal if is_negative else hexadecimal


def main():
    """Función de ejecución principal."""
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]
    results = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                clean_line = line.strip()
                if not clean_line:
                    continue
                try:
                    num = float(clean_line)
                    # Convertimos a int para bases, ya que suelen ser enteros
                    val = int(num)
                    results.append((val, to_binary(val), to_hexadecimal(val)))
                except ValueError:
                    print(f"Error: Invalid data '{clean_line}' at line {line_num}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Preparar salida
    header = f"{'Number':<10} | {'Binary':<20} | {'Hexadecimal':<15}\n"
    separator = "-" * 55 + "\n"
    output = header + separator
    for val, b, h in results:
        output += f"{val:<10} | {b:<20} | {h:<15}\n"
    
    footer = f"\nExecution Time: {elapsed_time:.6f} seconds\n"
    final_output = output + footer

    print(final_output)

    with open("ConvertionResults.txt", "w", encoding='utf-8') as f:
        f.write(final_output)


if __name__ == "__main__":

    main()
