# Lab 10.19


# Define ItemToPurchase class.
class ItemToPurchase:

    # Define default constructor and initialize parameters
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

        # OBJ 1:
        # Add item_description attribute
        self.item_description = description

    # Define total() function
    def total(self):
        price = self.item_quantity * self.item_price
        return price

    # Define print_item_cost() method to display
    # item name, price, quantity, and total cost.
    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, self.total()))

    # Define print_item_description() function
    # Ex. output >>> Bottled Water: Deer Park, 12 oz.
    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))


# OBJ 2:
# Define ShoppingCart class.
class ShoppingCart:

    # Define constructor to initialize the shopping cart and its parameters
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # Define add_item() function
    # Needs to have an ItemToPurchase parameter
    def add_item(self, ItemToPurchase):

        # Append required object of ItemToPurchase class
        # in the cart_items list.
        self.cart_items.append(ItemToPurchase)

    # Define remove_item() function
    def remove_item(self, item_name):

        # Go through cart_items list using For Loop
        for object in self.cart_items:

            # If current object in cart_items list matches given
            # item name, then that item is removed from the list.
            if object.item_name == item_name:
                self.cart_items.remove(object)
                return  # Causes us to return from the function

        # If item not found in cart_items list then
        # provide a message
        print("\nItem not found in cart. Nothing removed.")

    # Define modify_item() function with ItemToPurchase parameter
    # Does not return anything
    def modify_item(self, ItemToPurchase):

        # Declare & initialize a boolean variable to false.
        item_found = False

        # Go through cart_items list using For Loop.
        for object in self.cart_items:

            # If object in cart_items list matches the given
            # item to modify, then the item_found variable will be True
            if object.item_name == ItemToPurchase.item_name:
                item_found = True

                # Prompt user to enter the new item quantity
                print("Enter the new quantity:")
                item_quantity = int(input())

                # Assign current object to the
                # ItemToPurchase object.
                ItemToPurchase = object

                # Set item quantity of ItemToPurchase object to
                # the value of the variable item_quantity
                ItemToPurchase.item_quantity = item_quantity

                # If item_description of the object ItemToPurchase is not
                # none, then modify the item_description value of current object
                if ItemToPurchase.item_description != "none":
                    object.item_description = ItemToPurchase.item_description

                # If item_price of ItemToPurchase object is not 0, then
                # modify item_price of current object
                if ItemToPurchase.item_price != 0:
                    object.item_price = ItemToPurchase.item_price

                # If item_quantity of ItemToPurchase object is not 0, then
                # modify the item-quantity of current object
                if ItemToPurchase.item_quantity != 0:
                    object.item_quantity = ItemToPurchase.item_quantity
            # If value of item_found variable is still false,
            # then item is not found.
            if item_found == False:
                print("\nItem not found in cart. Nothing modified.")



    # method to get the # of items in a cart
    def get_num_items_in_cart(self):
        print(len(self.cart_items))

    # method to return the total cost of all items in the cart
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for i in self.cart_items:
            cost = (i.item_quantity * i.item_price)
            total_cost += cost
        return total_cost

    # method to print the total cost of objects in cart.
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print('Number of Items: {}'.format(self.get_num_items_in_cart()))
            for i in self.cart_items:
                total = i.item_price * i.item_quantity
                print('{} {} @ ${} = ${}'.format(i.item_name, i.item_quantity, i.item_price, total))
            print('Total: ${}'.format(total_cost()))

    # method to print each items' description
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print()
        print('Item Descriptions')
        for i in self.cart_items:
            i.print_item_description()


if __name__ == "__main__":
    pass
