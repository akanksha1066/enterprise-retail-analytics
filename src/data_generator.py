import os
import random
import csv
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def generate_retail_data(output_path, num_records=50000):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    categories = {
        'Electronics': ['Smartphone', 'Laptop', 'Smartwatch', 'Headphones'],
        'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Sneakers'],
        'Home & Kitchen': ['Blender', 'Coffee Maker', 'Microwave', 'Cookware'],
        'Beauty': ['Lipstick', 'Foundation', 'Perfume', 'Skincare Kit']
    }
    
    payment_methods = ['Credit Card', 'UPI', 'Cash', 'Net Banking']
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Kolkata', 'Lucknow']

    print(f"Generating {num_records} retail transactions...")
    
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Transaction_ID', 'Timestamp', 'Customer_ID', 'City', 'Category', 'Product', 'Quantity', 'Price_Per_Unit', 'Payment_Method'])
        
        start_date = datetime.now() - timedelta(days=180)
        
        for i in range(num_records):
            tx_id = f"TXN-{1000000 + i}"
            timestamp = start_date + timedelta(minutes=random.randint(1, 260000))
            cust_id = f"CUST-{random.randint(1000, 5000)}"
            city = random.choice(cities)
            category = random.choice(list(categories.keys()))
            product = random.choice(categories[category])
            quantity = random.choice([1, 2, 3, 5])
            price = round(random.uniform(10.0, 1200.0), 2)
            payment = random.choice(payment_methods)
            
            writer.writerow([tx_id, timestamp.strftime('%Y-%m-%d %H:%M:%S'), cust_id, city, category, product, quantity, price, payment])
            
    print(f"Data successfully saved to {output_path}")

if __name__ == "__main__":
    generate_retail_data("data/raw/transactions.csv", num_records=50000)