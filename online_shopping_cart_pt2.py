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


if __name__ == "__main__":
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

