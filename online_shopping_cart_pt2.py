# Lab 10.17 + Lab 10.19

# Create "item to purchase" class
class ItemToPurchase:
    # Default constructor
    def __init__(self):
        # Initialize variables w/ default values
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'

    # Calculate item total
    def total(self):
        price = self.item_quantity * self.item_price
        return price

    # Print the items
    def print_item_cost(self):
        # Display item name, quantity, price, and total
        print('{} {} @ ${} = ${}'.format(self.item_name, int(self.item_quantity), int(self.item_price),
                                         int(self.total())))

    # TODO: finish Print item description function
    def print_item_description(self):
        print('')

# Create "shopping cart" class
class ShoppingCart:
    def __init__(self):
        # Initialize shopping cart variables with default values
        self.customer_name = 'none'
        self.current_date = 'January 1, 2016'
        self.cart_items = []

    # method to add an item to the shopping list
    def add_item(self):
        self.cart_items.append(ItemToPurchase)

    # method to remove an item from the shopping cart
    def remove_item(self, item_to_remove):

        tremove_item = False
        # loop to find the item in the cart
        for item in self.cart_items:
            if item.item_name == item_to_remove:
                self.cart_items.remove(item)
                tremove_item = True
                break
        # if not item not found
        if not tremove_item:
            print('Item not found in the card. Nothing removed')



    # Main section
if __name__ == "__main__":
    # Create item objects
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    # Prompt item1 details from user
    print('Item 1')
    item1.item_name = str(input('Enter the item name:\n'))
    item1.item_price = float(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    # Prompt item2 details from user
    print('Item 2')
    item2.item_name = str(input('Enter the item name:\n'))
    item2.item_price = float(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    # Call method to print item details
    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print()

    # Calculate total cost of both items
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    # Display the total cost
    print('Total: ${}'.format(int(total)))
