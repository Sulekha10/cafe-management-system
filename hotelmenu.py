#define the menu of restaurant
menu = {
    'Pizza' : 100,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80
}
print("Welcome to Python Restaurant.")
print("Pizza : Rs100\nPasta : Rs50\nBurger : Rs60\nSalad : Rs70\nCoffee : Rs80")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your ordered item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet.")
    
another_item = input("Do you want to order another item? (yes/no) : ")
if another_item.lower() == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Iteme {item_2} has been added to order.")
    else:
        print(f"Ordered item {item_2} is not available yet.")
    
print(f"The total amount of items to pay is {order_total}")