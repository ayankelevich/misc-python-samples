#List initaliation
l1 = [1, 2, 3, 7]
l1.append(4)
l1 += [5, 6]
l1.sort()  # does not return an object
l2 = sorted(l1, reverse=True)
l3 = list()

# LIST COMPREHENSIONS
# list of tuples with all compbinations
burgers = ["beef", "chicken"]
toppings = ["cheese", "beans"]
meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

menu = [
    ["egg", "spam"],
    ["biscuit", "egg"]
]
no_spam_2 = [meal if "spam" not in meal else "skpipped" for meal in menu]
print(no_spam_2)