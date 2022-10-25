# I've created a simple shopping cart to show how to add items to it and update the total cost of the cart.

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Store:
    def __init__(self):
        self.__cart = []

    def addToCart(self, item):
        self.__cart.append(item)

    def removeFromCart(self, index):
        self.__cart.pop(index)

    def calculateTotal(self):
        total = 0
        for item in self.__cart:
            total += item.price

        return total

    def displayCart(self):
        for i in range(0, len(self.__cart)):
            item = self.__cart[i]
            print(i, item.name)


store = Store()
store.displayCart()

print("Hello, welcome to our store")

while True:
    store.displayCart()
    store.calculateTotal()

    print("Press a to add item")
    print("Press r to remove item")
    print("Press x to exit")
    userInput = input("Please enter a command")
    if userInput == "x":
        break
    elif userInput == "a":
        itemName = input("Please give the item a name")
        price = int(input("Please provide a price"))
        store.addToCart(Item(itemName, price))
    elif userInput == "r":
        index = int(input("Please provide the index of the item to remove"))
        store.removeFromCart(index)
    else:
        print("Please enter a valid input")
