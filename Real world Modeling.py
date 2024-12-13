# 4. Real-World Modeling (Restaurant Menu)
# Restaurant menu with items and their prices
menu = {
    "Burger": 8.50,
    "Pizza": 12.00,
    "Salad": 7.00,
    "Pasta": 10.00,
    "Soda": 2.50
}

# Function to calculate the total cost of a list of items
def calculate_total(order):
    total = 0
    for item in order:
        if item in menu:
            total += menu[item]
        else:
            print(f"'{item}' is not on the menu.")
    return total

# Example order
order = ["Burger", "Pizza", "Soda", "Ice Cream"]

print("Your order:", order)
total_cost = calculate_total(order)
print(f"Total cost: ${total_cost:.2f}")
