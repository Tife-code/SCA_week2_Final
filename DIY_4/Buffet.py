Restaurant = ("Jollof Rice", "Fried Rice", "French fries", "Crispy chicken", "Spagetti")

for food in Restaurant:
    print(food)

'''Restaurant[3] = "Fried Chicken"
Trying to modify items of a tuple will output an error(TypeError)
TypeError: 'tuple' object does not support item assignment '''

Restaurant = ("French fries", "Cripsy fried Chicken", 'Spagetti', 'Full vegan Sandwich', 'Fruit salad')

print("\nThis is the revised menu for today: ")
for food in Restaurant:
    print(food)