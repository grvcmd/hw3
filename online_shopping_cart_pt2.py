# Lab 10.17

class ItemToPurchase:
    def __init__(self, name = 'none', price = 0, quantity = 0, description = 'none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def total(self):
        price = self.item_quantity * self.item_price
        return price

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, int(self.item_quantity), int(self.item_price),
                                         int(self.total())))

    # TODO: output should be >>> Bottled Water: Deer Park, 12 oz.
    def print_item_description(self):
        print(self.item_description)

class ShoppingCart:
    # constructor to initialize the shopping cart
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # method to an item to cart_items list
    def add_item(self, item_to_be_added):
        self.cart_items.append(item_to_be_added)
        return True

    # method to remove an item from cart_items list
    def remove_item(self, item_to_be_removed):
        if item_to_be_removed in self.cart_items:
            self.cart_items.remove(item_to_be_removed)
        else:
            print('Item not found in cart. Nothing removed.')

    # TODO: finish method to modify an item's quantity
    def modify_item(self, item_to_be_modified):
        if item_to_be_modified in self.cart_items:
            item_to_be_modified

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



if __name__ == "__main__":
    pass