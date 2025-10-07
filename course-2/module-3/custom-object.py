class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare")

pizza = Recipe("Pizza", ["cheese","bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne","sauce"], 55)

print(pizza.items)
print(pasta.items)

print(pizza.contents())

# Sample code
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")