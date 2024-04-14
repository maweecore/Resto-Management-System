menu = {
    "Hawaiian Delight": {"category": "Pizza", "price": 309},
    "Garden Harvest": {"category": "Pizza", "price": 249},
    "Hungarian Fiesta": {"category": "Pizza", "price": 189},
    "Baked Macaroni": {"category": "Pasta", "price": 140},
    "Carbonara": {"category": "Pasta", "price": 140},
    "Spaghetti": {"category": "Pasta", "price": 140},
    "Nachos": {"category": "Appetizer", "price": 119},
    "Cheesy Potato Fries": {"Appetizer": "Pizza", "price": 139},
    "Iced Tea": {"category": "Drinks", "price": 39},
    "Blue Lemonade": {"category": "Drinks", "price": 39},
    "Soda": {"category": "Drinks", "price": 29},
}

inventory = {
    "Hawaiian Delight": 55,
    "Garden Harvest": 50,
    "Hungarian Fiesta": 45,
    "Baked Macaroni": 35,
    "Carbonara": 30,
    "Spaghetti": 25,
    "Nachos": 40,
    "Cheesy Potato Fries": 55,
    "Iced Tea": 50,
    "Blue Lemonade": 50,
    "Soda": 60
}

tables = {
    1: {"capacity": 2, "status": "Available"},
    2: {"capacity": 3, "status": "Available"},
    3: {"capacity": 3, "status": "Available"},
    4: {"capacity": 4, "status": "Available"},
    5: {"capacity": 6, "status": "Available"},
    6: {"capacity": 6, "status": "Available"}
}

def manage_orders():
    print("Order Management: ")
    categories = ["Pizza", "Pasta", "Appetizers", "Drinks"]
    for category in categories:
        order_choice = input(f"Do you want to order from {category} category? (yes/no): ")
        if order_choice.lower() == 'yes':
            order_category(category)

def order_category(category):
    print(f"\n{category} Menu: ")
    for item, details in menu.items():
        if details.get("category") == category:
            print(f"{item} - ₱{details['price']}")
    ordered_category = False
    while True:
        order_item = input(f"Enter the name of the food item from {category} category (or 'no' if you don't to order): ")
        if order_item.lower() == 'no':
            break
        elif order_item in menu and menu[order_item].get("category") == category:
            quantity = int(input(f"Enter quantity for {order_item}: "))
            if order_item in inventory and inventory[order_item] >= quantity:
                inventory[order_item] -= quantity
                print(f"{quantity} {order_item} added to the order.")
                ordered_category = True
            else:
                print(f"Insufficient inventory for {order_item}. Please choose another item.")
        else:
            print("Invalid item or not from the selected category. Please choose from the menu.")
    if not ordered_category:
        print("No items ordered from this category.")

def manage_tables():
    print("Table Management: ")
    print("1. View Tables")
    print("2. Assign Tables")
    print("3. Change Table Status")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        view_tables()
        assign_table()
    elif choice == 2:
        assign_table()
    elif choice == 3:
        change_table_status()
        assign_table()
    else:
        print("Invalid choice. Please enter a valid option.")

def view_tables():
    print("Tables: ")
    for table_num, details in tables.items():
        print(f"Table {table_num}: Capacity - {details['capacity']}, Status - {details['status']}")

def assign_table():
    print("Tables available for assignment: ")
    available_tables = [table_num for table_num, details in tables.items() if details['status'] == 'Available']
    for table_num in available_tables:
        print(f"Table {table_num}")
    table_num = int(input("Enter the table number to assign: "))
    if table_num in tables and tables[table_num]['status'] == 'Available':
        tables[table_num]['status'] = 'Occupied'
        print(f"Table {table_num} assigned successfully.")
    else:
        print("Invalid table number of already occupied.")

def change_table_status():
    table_num = int(input("Enter the table number to change status: "))
    if table_num in tables:
        new_status = input("Enter the new status (Available/Occupied): ")
        if new_status.lower() in ['available', 'occupied']:
            tables[table_num]['status'] = new_status.capitalize()
            print(f"Status of Table {table_num} changed to {new_status.capitalize()}.")
        else:
            print("Invalid status. Please enter 'Available' or 'Occupied'.")
    else:
        print("Invalid table number.")

def make_payment():
    total_amount = sum(menu[item]['price'] for item in menu)
    print(f"Total amount: ₱{total_amount}")
    while True:
        payment_option = input("Select payment option (cash/card): ")
        if payment_option.lower() == "cash":
            amount_paid = float(input("Enter the amount paid: ₱"))
            if amount_paid >= total_amount:
                change = amount_paid - total_amount
                print(f"Change: ₱{change}")
                print("Paymenr successful.")
                break
            else:
                print("Insufficient amount. Please enter a higher amount.")
        elif payment_option.lower() == "card":
            print("Payment successful.")
            break
        else:
            print("Invalid payment option. Please choose 'cash' or 'card'.")

def main():
    print("Welcome to the Reastaurant Management System!")
    print("1. Cashier Sign In")
    print("2. Admin Log-in")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        manage_orders()
        manage_tables()
        make_payment()
    elif choice == 2:
        admin_username = "admin"
        admin_password = "admin123"
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == admin_username and password == admin_password:
            print("Admin logged on successfully.")
            admin_menu()
        else:
            print("Invalid username or password.")

def admin_menu():
    print("Admin Menu: ")
    print("1. Menu Mangement")
    print("2. Inventory Manaement")
    print("3. Table Management")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        manage_menu()
    elif choice == 2:
        manage_inventory()
    elif choice == 3:
        admin_manage_tables()
    else: 
        print("Invalid choice. Please enter a valid option.")

def manage_menu():
    print("Menu Management: ")
    print("1. Add Item to Menu")
    print("2. Remove Item from Menu")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item_to_menu()
    elif choice == 2:
        remove_item_from_menu()
    else: 
        print("Invalid choice. Please enter a valid option.")

def add_item_to_menu():
    item_name = input("Enter the name of the new item: ")
    if item_name in menu:
        print("Item already exists in the menu.")
        return
    category = input("Enter the category of the item: ")
    price = float(input("Enter the price of the item: "))
    menu[item_name] = {"category": category, "price": price}
    print(f"{item_name} added to the menu.")

def remove_item_from_menu():
    item_name = input("Enter the name of the item to remove: ")
    if item_name in menu:
        del menu[item_name]
        print(f"{item_name} removed from the menu.")
    else:
        print("Item not found in the menu.")

def manage_inventory():
    print("Inventory Management: ")
    print("1. Add Item to Inventory")
    print("2. Remove Item from Inventory")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item_to_inventory()
    elif choice == 2:
        remove_item_from_inventory()
    else: 
        print("Invalid choice. Please enter a valid option.")

def add_item_to_inventory():
    item_name = input("Enter the name of the new item: ")
    if item_name in inventory:
        print("Item already exists in the inventory.")
        return
    quantity = int(input("Enter the quantity of the item to add: "))
    inventory[item_name] = quantity
    print(f"{quantity} {item_name} added to the inventory.")

def remove_item_from_inventory():
    item_name = input("Enter the name of the item to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print("Item not found in the inventory.")

def admin_manage_tables():
    print("Table Management: ")
    print("1. Add Table")
    print("2. Remove Table")
    print("3. Modify Table Details")
    print("4. View Table Availability")
    choice = int(input("Enter your chouce: "))
    if choice == 1:
        add_table()
    elif choice == 2:
        remove_table()
    elif choice == 3:
        modify_table_details()
    elif choice == 4:
        view_table_availability()
    else: 
        print("Invalid choice. Please enter a valid option.")
    
def add_table():
    table_num = int(input("Enter the table number to add: "))
    if table_num in tables:
        print("Table already exists.")
        return
    capacity = int(input("Enter the capacity of the table: "))
    status = input("Enter the status of the table (Available/Occupied): ").capitalize()
    tables[table_num] = {"capacity": capacity, "status": status}
    print(f"Table {table_num} added succsfully.")

def remove_table():
    table_num = int(input("Enter the table number to remove: "))
    if table_num in tables:
        del tables[table_num]
        print(f"Table {table_num} removed successfully.")
    else:
        print("Table not found.")

def modify_table_details():
    table_num = int(input("Enter the table number to modify: "))
    if table_num in tables:
        capacity = int(input("Enter the new capacity of the tablle: "))
        status = input("Enter the new status of the table (Available/Occupied): ").capitalize()
        tables[table_num]["capacity"] = capacity
        tables[table_num]["status"] = status
        print(f"Details of Table {table_num} modified successfully.")
    else:
        print("Table not found.")

def view_table_availability():
    print("Table Availability: ")
    for table_num, details in tables.items():
        print(f"Table {table_num}: Capacity - {details['capacity']}, Status - {details['status']}")

main()