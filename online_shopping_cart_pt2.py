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

    # Define get_num_items_in_cart() function
    def get_num_items_in_cart(self):

        # Declare & initialize total_quantity to 0.
        # This is where total quantity of the cart will be stored.
        total_quantity = 0

        # Go through cart_items list using For Loop
        for object in self.cart_items:
            total_quantity += object.item_quantity

        # Return total_quantity variable
        return total_quantity

    # Define get_cost_of_cart() function
    def get_cost_of_cart(self):

        # Declare & initialize total_cost variable to 0.
        # This is where total cost of the cart will be stored.
        total_cost = 0

        # Go through cart_items list using For Loop
        for object in self.cart_items:
            total_cost += object.item_price * object.item_quantity

        # Return total cost of the cart.
        return total_cost

    # Define print_total() function
    def print_total(self):

        # If length of cart_items list is not 0
        if len(self.cart_items) != 0:

            # Display the title of the shopping cart.
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))

            # Display number of items in the cart by calling
            # the get_num_items_in_cart() function.
            print("Number of items: {}".format(self.get_num_items_in_cart()))
            print()

            # Go through cart_items list using a For Loop
            for object in self.cart_items:
                # Call print_item_cost() function for each object
                # in the cart_items list
                object.print_item_cost()

            # Display the total cost of the cart by calling the
            # get_cost_of_cart() function.
            print("Total: ${}".format(self.get_cost_of_cart()))

        # If cart is empty display 'SHOPPING CART IS EMPTY'
        else:
            print("\nSHOPPING CART IS EMPTY")

    # Define print_descriptions function
    def print_descriptions(self):

        # Display the title of the cart.
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))

        # Display item_description for each object in the cart_items list
        # by going through the list using a For Loop and
        # calling the print_item_description() function
        print("\nItem Descriptions")
        for object in self.cart_items:
            object.print_item_description()

# Define menuOfChoices():
def menuOfChoices():

    # Display the menu
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")


# OBJ 4:
# Define the print_menu() function
def print_menu(self):

    # Declare & initialize required variable to store user choice
    choice = ''

    # Call the menuOfChoices() function to display the menu of choices
    menuOfChoices()

    # Prompt user to enter an option
    choice = input("\nChoose an option: ")

    # While Loop until the user's choice is q for Quit
    while choice != 'q':

        # OBJ 7:
        # If the user's choice is (a)
        if choice == 'a':
            print("ADD ITEM TO CART")

            # Prompt user to enter the item's
            # name, price, quantity, and description.
            print("Enter the item name:")
            item_name = input()
            print("Enter the item description:")
            item_description = input()
            print("Enter the item price:")
            item_price = int(input())
            print("Enter the item quantity:")
            item_quantity = int(input())

            # Create an object of the ItemToPurchase class
            # and pass the required parameters
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)

            # Call add_item() function and pass the object
            # of the ItemToPurchase class.
            self.add_item(item)

        # OBJ 8:
        # if user choice is (r)
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")

            # Prompt user to enter the item_name
            print("Enter name of item to remove:")
            item_name = input()

            # Call the remove_item() function and pass the item_name
            # the user specified
            self.remove_item(item_name)

        # OBJ 9:
        # If user choice is (c)
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")

            # Prompt user to enter the item_name
            print("Enter the item name:")
            item_name = input()

            # Create an object of the ItemToPurchase class by passing the item_name
            # to as the parameter
            item = ItemToPurchase(item_name)

            # Call the modify_item() function and pass
            # the ItemToPurchase object
            self.modify_item(item)

        # OBJ 6:
        # If the user choice is (i) call the print_descriptions() function
        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            self.print_descriptions()

        # OBJ 5:
        # if the user choice is (o), call the print_total() function
        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            self.print_total()

        # Call function menuOfChoices() and prompt
        # user to enter another option
        menuOfChoices()
        choice = input("Choose an option: ")


# OBJ 3:
# Define the main() function.
def main():

    # Prompt user to enter customer_name and current_date
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:\n")
    current_date = input()

    # Create an object of the ShoppingCart class
    # by passing the parameters
    mycart = ShoppingCart(customer_name, current_date)

    # Display customer_name and current_date
    print("Customer name: {}".format(mycart.customer_name))
    print("Today's date: {}".format(mycart.current_date))

    # Call print_menu() function and [ass the
    # object of the ShoppingCart class.
    print_menu(mycart)

# Call the main() function to start the program.
main()
