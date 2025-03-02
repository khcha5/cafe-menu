def display_menu():
    print("Welcome to Our Café!")
    print("1. Coffee")
    print("2. Pastries")
    print("3. Teas")
    print("4. Exit")

def show_coffee_menu():
    print("\nCoffee Menu:")
    coffee_items = {
        "Espresso": 2.50,
        "Cappuccino": 3.00,
        "Latte": 3.50
    }
    for item, price in coffee_items.items():
        print(f"{item}: ${price:.2f}")
    
def show_pastries_menu():
    print("\nPastries Menu:")
    pastry_items = {
        "Croissant": 2.00,
        "Blueberry Muffin": 2.50,
        "Chocolate Cake": 3.00
    }
    for item, price in pastry_items.items():
        print(f"{item}: ${price:.2f}")

def show_tea_menu():
    print("\nTea Menu:")
    tea_items = {
        "Green Tea": 2.00,
        "Chai Latte": 3.00,
        "Herbal Tea": 2.50,
        "milk"       :4
    }
    for item, price in tea_items.items():
        print(f"{item}: ${price:.2f}")

def main():
    while True:
        display_menu()
        choice = input("\nPlease choose a category (1-4): ")

        if choice == '1':
            show_coffee_menu()
        elif choice == '2':
            show_pastries_menu()
        elif choice == '3':
            show_tea_menu()
        elif choice == '4':
            print("Thank you for visiting! Have a great day!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
