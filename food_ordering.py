print("🍔 Food Ordering System")

menu = {
    1: {"name": "Burger", "price": 120},
    2: {"name": "Pizza", "price": 250},
    3: {"name": "Biryani", "price": 180},
    4: {"name": "Fried Rice", "price": 150},
    5: {"name": "Ice Cream", "price": 80}
}

cart = []

while True:
    print("\n1. View Food Menu")
    print("2. Add Food Item")
    print("3. View Cart")
    print("4. Remove Food Item")
    print("5. Calculate Total Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n🍽️ Food Menu")

        for number, item in menu.items():
            print(
                number,
                "-",
                item["name"],
                "- ₹",
                item["price"]
            )

    elif choice == "2":
        number = int(input("Enter food item number: "))

        if number in menu:
            quantity = int(input("Enter quantity: "))

            item = {
                "name": menu[number]["name"],
                "price": menu[number]["price"],
                "quantity": quantity
            }

            cart.append(item)

            print("✅ Item added to cart!")

        else:
            print("❌ Invalid food item.")

    elif choice == "3":
        if len(cart) == 0:
            print("🛒 Cart is empty.")
        else:
            print("\n🛒 Your Cart")

            for item in cart:
                total = item["price"] * item["quantity"]

                print("--------------------")
                print("Item:", item["name"])
                print("Price:", item["price"])
                print("Quantity:", item["quantity"])
                print("Total:", total)

    elif choice == "4":
        item_name = input("Enter food item name to remove: ")

        found = False

        for item in cart:
            if item["name"].lower() == item_name.lower():
                cart.remove(item)
                print("✅ Item removed from cart!")
                found = True
                break

        if not found:
            print("❌ Item not found in cart.")

    elif choice == "5":
        if len(cart) == 0:
            print("🛒 Cart is empty.")
        else:
            grand_total = 0

            for item in cart:
                grand_total += item["price"] * item["quantity"]

            print("\n🧾 Total Bill")
            print("Grand Total: ₹", grand_total)

    elif choice == "6":
        print("Thank you for using Food Ordering System! 🍔")
        break

    else:
        print("❌ Invalid choice!")
