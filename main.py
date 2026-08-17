from functions import load_purchases, calculate_revenue, most_expensive_item, highest_sold_products

records                 = load_purchases("data.txt")
revenue                 = calculate_revenue(records)
expensive_item          = most_expensive_item(records)
highest_selling_product = highest_sold_products(records)

print(highest_selling_product)