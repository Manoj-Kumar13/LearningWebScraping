# using escape character
print("we are also called \"vikings\" from north")

# using variables
name = 'python'
version = 3.0
installed = True
print(name, version, installed)

# typecasting in python
int1 = 1
int2 = 2
print(str(int1) + str(int2))

# taking input
# name = input("what is your name? : ")
# print("Hi,", name)

# receiving an integer input
current_year = 2023
# age = int(input("what is your age? : "))
# print(f"your born year is either {current_year - age}  or {current_year - age - 1}")

# using pre-built methods
name = 'joHn doe'
print(name)
print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())

# arithmatic operations in python
print(f"float division {4 / 2}")
print(f"interger division {4 // 2}")
print(f"multiplication {4 * 3}")
print(f"power {4 ** 3}")

# importing libraries
import math

int1 = 5.2
print(math.floor(int1))
print(int1.__floor__())

# using if statements
is_snowing = False

if is_snowing:
    print(f"""Hello {name.title()},
It's snowing out there!
have a good day""")
elif not is_snowing:
    print("you should go outside")
else:
    print("It's not snowing outside")

# AND OR NOT operators
temp = 20
if is_snowing and temp==20:
    print("condition satisfied")
elif (not is_snowing) and (temp==20):
    print("condition partially satisfied")
else:
    print("condition not satisfied")

# Lists in python
people = ["Allen", "Michael", "John", "Ben"]
# people = people[0:3]
print(people)

# List operations

# people.append(5)
# people.remove("Allen")
people.sort()
print(people)

import random
print(random.choice(people))

# List - []
# Tuples - () - Tuples are immutable lists, working is almost same

# Dictionaries in python
friend = {
    "name" : "Maike",
    "age" : 25,
    "gender": "Male",
}

print(friend.get("name"))
print(list(friend.keys()))
print(list(friend.values()))

# range function gives all the numbers between specified range
print(list(range(10)))

# for loops in python
find = "Allen"

# 1st solution
for person in people:
    if person == find:
        print(f"{person} found using loop")
        break #break is used to stop the loop

# 2nd solution
if find in people:
    print(f"{find} is my found using if statement")

budget = 100
price = 10
items = 0
# find how many items we can buy
while budget>0:
    budget -= price
    items+=1

print(f"we can buy {items} items")

# functions in python
def special_count(stop_count, step=1    ):
    for x in range(1,stop_count+1, step):
        print(x)

special_count(stop_count=5, step=2)

# hide initial numbers of 16 digit card
def hideCard(number):
    newNum = "**********"
    newNum += number[12 :]
    return newNum

result = hideCard('1234567890123456')
print(result)

# classes in python
class CreditCard:
    # creating a constructor
    raise_limit = 1.5
    def __init__(self, number, limit=1000, company='ABC'):
        self.number = number
        self.limit = limit
        self.company = company
    def raise_card_limit(self):
        # self.limit *= self.raise_limit alternatve way
        self.limit *= CreditCard.raise_limit
        self.limit = int(self.limit)


# my_card = CreditCard()
# my_card.number = '1234567890123456'
# my_card.limit = 5000
# my_card.company = "abc"
# print(my_card.number)
# print(my_card.limit)
# print(my_card.company)

c1 = CreditCard(number='1234567890123456', limit=5000, company='ABC')
c2 = CreditCard(number='5678901234567890', limit=7000, company='CDE')
c3 = CreditCard(number='9012345678901234', limit=3000, company='XYZ')

print(c1.number, c1.limit, c1.company)
print(c2.number, c2.limit, c2.company)
c3.raise_card_limit()
print(c3.number, c3.limit, c3.company)

class Item:
    # setting expected data-type
    def __init__(self, name:str, price: int =100, quantity: int =0):
        # run validations on received arguments
        assert price>=0, f"price can not be negative"
        assert quantity>=0, f"quantity can not be negative"

        # setting values
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item("phone",1,1)

print(item1.name, item1.price, item1.quantity)

# getting all the available attributes
print(Item.__dict__)
print(item1.__dict__)