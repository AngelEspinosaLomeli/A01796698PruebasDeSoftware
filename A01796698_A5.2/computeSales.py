# pylint: disable=invalid-name
"""
Compute Sales Program
Calculates total sales based on a price catalogue and a sales record.
"""

import sys
import json
import time


def load_json_file(file_path):
    """Loads a JSON file and handles basic file errors."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON.")
    except OSError as e:
        print(f"OS error occurred: {e}")
    return None


def calculate_total_sales(catalogue, sales):
    """Computes total cost and tracks errors in data."""
    price_map = {item['Product']: item['Price'] for item in catalogue
                 if 'Product' in item and 'Price' in item}

    total_cost = 0.0
    errors = []

    for sale in sales:
        product_name = sale.get('Product')
        quantity = sale.get('Quantity')

        if product_name in price_map:
            try:
                price = price_map[product_name]
                total_cost += float(price) * float(quantity)
            except (ValueError, TypeError):
                errors.append(f"Invalid numeric data for sale: {sale}")
        else:
            errors.append(f"Product '{product_name}' not found in catalogue.")

    return total_cost, errors


def main():
    """Main execution flow."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json "
              "salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    # Load files
    catalogue_data = load_json_file(sys.argv[1])
    sales_data = load_json_file(sys.argv[2])

    if catalogue_data is None or sales_data is None:
        sys.exit(1)

    # Process data
    total_cost, errors = calculate_total_sales(catalogue_data, sales_data)

    # Handle errors (Req 3)
    if errors:
        print("\n--- Processing Errors ---")
        for error in errors:
            print(error)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Format output (Req 2 & 7)
    results_output = (
        f"{'='*30}\n"
        f" SALES EXECUTION RESULTS\n"
        f"{'='*30}\n"
        f"Total Sales Cost: ${total_cost:,.2f}\n"
        f"Time Elapsed:     {elapsed_time:.4f} seconds\n"
        f"{'='*30}\n"
    )

    # Print to screen
    print(f"\n{results_output}")

    # Save to file
    try:
        with open("SalesResults.txt", "w", encoding='utf-8') as f:
            f.write(results_output)
    except IOError as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
