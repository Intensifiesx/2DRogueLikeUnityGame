
# Updated: Documented Script: Grocery_List.py
class GroceryItem:
    """
    Represents a single grocery item.
    
    Attributes:
        name (str): The name of the grocery item.
        price (float): The price per unit of the grocery item.
    """
    def __init__(self, name, price):
        """
        Initializes a new GroceryItem instance.
        
        Parameters:
            name (str): The name of the grocery item.
            price (float): The price per unit of the item.
        """
        self.name = name
        self.price = price

class GroceryCalculator:
    """
    Manages a collection of GroceryItem objects and calculates the total cost.
    
    Attributes:
        items (list): A list of tuples, each containing a GroceryItem object and its quantity.
    """
    def __init__(self):
        """
        Initializes a new GroceryCalculator instance.
        """
        self.items = []

    def add_item(self, item, quantity):
        """
        Adds a new item along with its quantity to the list.
        
        Parameters:
            item (GroceryItem): The grocery item to add.
            quantity (int): The quantity of the grocery item.
        """
        self.items.append((item, quantity))

    def calculate_total_cost(self):
        """
        Calculates the total cost of all items in the list.
        
        Returns:
            float: The total cost of the groceries.
        """
        total_cost = 0
        for item, quantity in self.items:
            total_cost += item.price * quantity
        return total_cost

def main():
    """
    Main function to run the Grocery Calculator application.
    """
    calculator = GroceryCalculator()
    
    while True:
        item_name = input("Enter the grocery item name (or type 'done' to finish): ").strip()
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
