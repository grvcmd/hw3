# Lab 10.17

class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def total(self):
        price = self.item_quantity * self.item_price
        return price

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, int(self.item_quantity), int(self.item_price), int(self.total())))

if __name__ == "__main__":
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    print('Item 1')
    item1.item_name = str(input('Enter the item name:\n'))
    item1.item_price = float(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    print('Item 2')
    item2.item_name = str(input('Enter the item name:\n'))
    item2.item_price = float(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print()

    # Calculate the cost of items
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    # Display the total cost
    print('Total: ${}'.format(int(total)))