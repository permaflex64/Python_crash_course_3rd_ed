# Lista ordini vuota
orders = []

# Menu con prezzi
menu = {
    'margherita': 8.50,
    'pepperoni': 10.00,
    'hawaiian': 11.50,
}

total = 0

# Ciclo principale
while True:
	order = input("Enter pizza name (or 'done' to finish):  ")
	if order == "done":
		break
	elif order in menu:
		orders.append(order)
		total += menu[order]
	else:
		print(f"Sorry, we don't have {order} on the menu.")

# Rimuovi un ordine        
remove_order = input("Remove any item? (yes/no): ")
if remove_order == "yes":
    for order in orders:
        print(f"{order}: ${menu[order]}")
    order_to_remove = input("What item would you like to remove? ")
    if order_to_remove in orders:
        orders.remove(order_to_remove)
        total -= menu[order_to_remove]
        print(f"{order_to_remove} has been removed from your order.")
    else:
        print(f"{order_to_remove} is not in your order.")
     
        
# Stampa ordini
print("--- Your Order ---")

for pizza in orders:  # o 'item', 'pizza_name'
    print(f"{pizza}: ${menu[pizza]}")
		
print("---")
#print(f"Total: ${sum(menu[order] for order in orders)}")
print(f"Total: ${total}")
print("Thank you for your order!")