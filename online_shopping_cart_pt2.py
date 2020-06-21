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

# ------------------------------------------------------------------------------------

# Create "shopping cart" class
class ShoppingCart:
    def __init__(self):
        # Initialize shopping cart variables with default values
        self.customer_name = 'none'
        self.current_date = 'January 1, 2016'
        self.cart_items = []

    #  TODO: finish method to add an item to the shopping cart
    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    # TODO: finish method to remove an item from the shopping cart
    def remove_item(self, item_to_remove):

        tremove_item = False
        # loop to find the item in the shopping cart
        for item in self.cart_items:
            if item.item_name == item_to_remove:
                self.cart_items.remove(item)
                tremove_item = True
                break
        # if item not found in the shopping cart
        if not tremove_item:
            print('Item not found in cart. Nothing removed')


    # TODO: finish method to modify quantity of an item in the shopping cart
    def modify_item(self, itemToPurchase):

        tmodify_item = False
        # loop to find an item in the shopping cart
        for i in range(len(self.cart_items)):

            if self.cart_items[i].item_name == itemToPurchase.item_name:
                tmodify_item = True
                self.cart_items[i].item_quantity = itemToPurchase.item_quantity
                break

        # if item not found in shopping cart
        if not tmodify_item:
            print('Item not found in cart. Nothing modified.')


# --------------------------------------------------------------------------------------------

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
