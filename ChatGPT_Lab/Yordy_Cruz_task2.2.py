# Original code: Grocery_List.py
class GroceryItem:
    # Represents a grocery item with a name and price per unit.
    def __init__(self, name, price):
        self.name = name
        self.price = price

class GroceryCalculator:
    # Manages a collection of grocery items and calculates the total cost.
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def calculate_total_cost(self):
        total_cost = 0
        for item, quantity in self.items:
            total_cost += item.price * quantity
        return total_cost

def main():
    calculator = GroceryCalculator()
    
    while True:
        item_name = input("Enter the grocery item name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_price = float(input(f"Enter the price for {item_name}: "))
        item_quantity = int(input(f"Enter the quantity for {item_name}: "))
        
        item = GroceryItem(item_name, item_price)
        calculator.add_item(item, item_quantity)
    
    total_cost = calculator.calculate_total_cost()
    print(f"Total cost of groceries: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
