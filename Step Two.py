class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

# First item
print("Item 1")
item1_name = input("Enter the item name: ")
item1_price = float(input("Enter the item price: "))
item1_quantity = int(input("Enter the item quantity: "))
item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

# Second item
print("\nItem 2")
item2_name = input("Enter the item name: ")
item2_price = float(input("Enter the item price: "))
item2_quantity = int(input("Enter the item quantity: "))
item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

# Print item costs
item1.print_item_cost()
item2.print_item_cost()
