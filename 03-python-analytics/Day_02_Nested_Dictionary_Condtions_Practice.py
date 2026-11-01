sales = {
    "Laptop": {
        "category": "Electronics",
        "quantity": 2,
        "revenue": 90000
    },
    "Mouse": {
        "category": "Accessories",
        "quantity": 5,
        "revenue": 2500
    },
    "Office Chair": {
        "category": "Furniture",
        "quantity": 4,
        "revenue": 14000
    },
    "Monitor": {
        "category": "Electronics",
        "quantity": 2,
        "revenue": 24000
    }
}

# Print the product names which have the sales quantity more than 3

for product, details in sales.items():
    if details['quantity'] > 3:
        print(product)

# Print the product names and their respective revenues, the product must belong to electronics category and revenue should be greater than 10000

for product, details in sales.items():
    if details['category'] == "Electronics" and details['revenue'] > 10000:
        print(f"{product} - {details['revenue']}")

# Print the product names with their respective quantity and revenues for products belong to Accessories category and quantity should be greater than 3

for product, details in sales.items():
    if details['category'] == "Accessories" and details['quantity'] > 3:
        print(f"{product} - Quantity: {details['quantity']}, Revenue: ₹{details['revenue']:,}")

# Print the products belong to Electronics or quantity more than 3
for product, details in sales.items():
    if details['category'] == "Electronics" or details['quantity'] > 3:
        print(f"{product}")