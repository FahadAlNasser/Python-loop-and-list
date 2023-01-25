# -*- coding: utf-8 -*-
food_truck = ["Chinese Express", "Italian Pizza", "Sam's Humburger"]
type_of_food = ["Chinese", "Italian", "American"]
user_input = input("What is your favorite food truck?")
us_input = input('What is your favorite type of dishes?')
print((f'my favorite type of food is {user_input.lower()} and my favorite food truck is {us_input.lower()}'))

"""Section 2"""

for counting in range(41):
  if counting % 3 == 0 or counting % 5 == 0:
    print(f"{counting} is divisible by 3 or 5")
  else:
    print(f"{counting} is not divisible by 3 or 5")

"""Section 3"""

Shows = ['Arrow', 'Teenwolf', ' Supergirl', 'Supernatural', 'Charmed']
show = input('What is your favorite show?')
print(Shows)
for x in Shows:
  print(f'My favorite shows {x}')
Shows.append(show)
del Shows[0]
print(Shows)

"""Section 4"""

ceb = ['Rita Ora', 'Chris Hemsworth', 'Demi Lovato']
def celebrity(name, namo):
  print(f'names: {name[0:4]}{namo[1:4]}')
celebrity (ceb[0], ceb[1])
celebrity (ceb[1], ceb[1])
celebrity (ceb[2], ceb[0])

"""Section 5"""

dictionary = {'S': 'Steak', 'I': 'Ice cream', 'G': 'Grilled chicken', 'V': 'Vegatables'}
print(dictionary)
User = input ('Please type a first letter')
if User == 'S':
  print(f'The letter S is for Steak ')
