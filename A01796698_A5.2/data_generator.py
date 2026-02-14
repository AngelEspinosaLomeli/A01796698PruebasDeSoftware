import json
import random

def generate_test_data():
    # 1. Crear un catálogo de 100 productos diferentes
    products = [f"Product_{i}" for i in range(1, 101)]
    catalogue = []
    for p in products:
        catalogue.append({
            "Product": p,
            "Price": round(random.uniform(10.0, 500.0), 2)
        })

    # 2. Crear un registro de 5,000 ventas aleatorias
    sales = []
    for _ in range(5000):
        sales.append({
            "Product": random.choice(products),
            "Quantity": random.randint(1, 10)
        })
    
    # 3. Agregar algunos datos erróneos a propósito (para probar Req 3)
    sales.append({"Product": "NonExistentItem", "Quantity": 1})
    sales.append({"Product": "Product_1", "Quantity": "InvalidValue"})

    # Guardar archivos
    with open('large_catalogue.json', 'w') as f:
        json.dump(catalogue, f, indent=4)
    
    with open('large_sales.json', 'w') as f:
        json.dump(sales, f, indent=4)

    print("Archivos 'large_catalogue.json' y 'large_sales.json' generados con éxito.")

if __name__ == "__main__":
    generate_test_data()