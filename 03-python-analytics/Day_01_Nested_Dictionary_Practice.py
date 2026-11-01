sales = {
    "Laptop": {
        "quantity": 2,
        "price": 45000
    },
    "Mouse": {
        "quantity": 5,
        "price": 500
    }
}

# Caluclating and adding revenue using the sales dicionary
for product, details in sales.items():
    details['revenue'] = details['quantity'] * details['price']

# Total Number of transactions 
total_transactions = len(sales)
print(f"Total Number of sales are {total_transactions}")

# Caluclate the total revenue
total_revenue = 0
for product, details in sales.items():
    total_revenue += details['revenue']
print(f"Total revenue is {total_revenue}")

# Caluclate the avearage of total revenue
avg_revenue = 0
for product, details in sales.items():
    avg_revenue = total_revenue / len(sales)

print(f"Avearge of total revenue is {avg_revenue}")

# Find the product with least revenue
min_revenue = sales['Laptop']['quantity'] * sales['Laptop']['price']
min_product = "Laptop"
for product, details in sales.items():
    if min_revenue > details['revenue']:
        min_revenue = details['revenue']
        min_product = product

print(f"{min_product} is with Min Revenue of {min_revenue}")

# Find the product with highest revenue
max_revenue = 0
max_product = ""
for product, details in sales.items():
    if max_revenue < details['revenue']:
        max_revenue = details['revenue']
        max_product = product

print(f"{max_product} is with Max Revenue of {max_revenue}")