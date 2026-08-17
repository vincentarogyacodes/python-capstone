from purchase import Purchase

def load_purchases(filename):
    records = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            record = Purchase(parts[0], parts[1], parts[2])
            records.append(record)
        return records

def calculate_revenue(records):
        revenue = 0
        for r in records:
            cost = float(r.price)
            revenue += cost
        return revenue

def most_expensive_item(records):
    expensive_item = records[0]
    for record in records:
        if float(record.price) > float(expensive_item.price):
            expensive_item = record         
    return expensive_item.item

def highest_sold_products(records):
    highest_selling_product = {}
    for record in records:
        if record.item not in highest_selling_product:
            highest_selling_product[record.item] = float(record.price)
        else:
            highest_selling_product[record.item] += float(record.price)
    return highest_selling_product