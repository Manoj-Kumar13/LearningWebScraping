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

# another way of taking input
# print("Hello " + input("what is your name?"))

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
print(f"integer division {4 // 2}")
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

# for working with csv
import csv
class Item:
    all = []
    # setting expected data-type
    def __init__(self, name:str, price: int =100, quantity: int =0):
        # run validations on received arguments
        assert price>=0, f"price can not be negative"
        assert quantity>=0, f"quantity can not be negative"

        # setting values
        self.name = name
        self.price = price
        self.quantity = quantity

        # keeping all instances
        Item.all.append(self)

        # representing the instances
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity} )"

    # working with class methods
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity= int(item.get('quantity')),
            )

    # working with static methods
    @staticmethod
    def is_integer(num):
        # check the floats which are point zero
        if isinstance(num, float):
            # check if the floats are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

# getting all the available attributes
# print(Item.__dict__)

# Item.instantiate_from_csv()
# print(Item.is_integer(7.0))

print(Item.all) # using repr method

# for instance in Item.all:
#     print(instance.name)

# round function is used to round-off the value upto certain decimal places
print(round(2.545454,2))

# round number to certain decimal places using formatting
bill_amount = 5
print("{:.2f}".format(bill_amount))

# min max function in python
arr = [2,5,8,2,47,9,1]

print(f"max in arr {max(arr)}")
print(f"min im arr {min(arr)}")

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_len = len(letters)
numbers_len = len(numbers)
symbols_len = len(symbols)

letters_gen = ""

for x in range(nr_letters-nr_symbols-nr_numbers):
  letter_index = random.randint(0,letters_len-1)
  letters_gen += letters[letter_index]

symbols_gen = ""
for x in range(nr_symbols):
  symbol_index = random.randint(0,symbols_len-1)
  symbols_gen += symbols[symbol_index]

number_gen = ""
for x in range(nr_numbers):
  number_index = random.randint(0,numbers_len-1)
  number_gen += numbers[number_index]

password = letters_gen + symbols_gen + number_gen
print("Easy password",password)



#Hard Level - Order of characters randomised:
temp_list = list(password)
random.shuffle(temp_list)
print("Hard password",''.join(temp_list))
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P