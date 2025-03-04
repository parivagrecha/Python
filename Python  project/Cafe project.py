# Define the menu of Cafe
menu = {
    'pizza': 40,
    'pasta':50,
    'burger':35,
    'salad':20,
    'coffee':45,
}

# Greet
print ("Welcome to python cafe")
print ("pizza: rs40\n, pasta: rs50\n, burger: rs35\n, salad: rs20\n, coffee: rs45\n")

order_total = 0

item_1 = input("Enter the name of item which you want =")
if item_1 in menu :
    order_total +=menu[item_1]
    print(f"your item {item_1} has been added to your order")

else :
    print(f"Please order something else order item {item_1} is not available yet")

another_order = input("do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the name of item 2 which you want =")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"your item {item_2} has been added to your order")

    else :
        print(f"Please order something else order item {item_2} is not available yet")

print(f" The total amount of item is {order_total}")


