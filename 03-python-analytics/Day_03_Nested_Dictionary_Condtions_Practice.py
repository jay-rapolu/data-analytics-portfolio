sales = {
    "T001": {"product": "Laptop", "revenue": 90000},
    "T002": {"product": "Mouse", "revenue": 0},
    "T003": {"product": "Keyboard", "revenue": None},
    "T004": {"product": "Monitor", "revenue": 24000}
}
for transaction, details in sales.items():
    revenue = details['revenue']
    if revenue is None:
        print(f"{transaction}: Missing revenue")
    elif revenue == 0:
        print(f"{transaction}: Zero revenue")
    elif revenue > 0:
        print(f"{transaction}: Positive revenue")    

transactions = [
    {"id": "T001", "product": "Laptop", "revenue": 90000},
    {"id": "T002", "product": "Mouse", "revenue": 2500},
    {"id": "T006", "product": "Office Desk", "revenue": 8000},
    {"id": "T006", "product": "USB Hub", "revenue": 3600},
    {"id": "T012", "product": "Keyboard", "revenue": None}
]

seen_ids = set()
for transaction in transactions:
    transaction_id = transaction['id']
    revenue = transaction['revenue']
    if transaction_id in seen_ids:
        print(f"{transaction_id} is repeated")
    else:
        seen_ids.add(transaction_id)
    if revenue is None:
        print(f"{transaction_id} has missing revenue")    